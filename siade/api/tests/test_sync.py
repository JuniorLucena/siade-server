# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from datetime import datetime, timedelta
from uuid import uuid4 as uuid
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from rest_framework.test import APITestCase
from rest_sync.serializers import ModelSyncSerializer, sync_serializer_factory
from siade.agentes.management import create_or_update_groups
from siade.api.serializers import serializer_factory
from siade.imoveis.models import *
from siade.trabalhos.models import *
from siade.agentes.tests.factories import *
from siade.imoveis.tests.factories import *
from siade.trabalhos.tests.factories import *


def adicionar_sync_state(obj):
    obj.update({
        'sync_version': '',
        'sync_changed': datetime.now(),
        'sync_deleted': False,
    })
    return obj


def remover_sync_state(obj):
    del obj['sync_version']
    del obj['sync_changed']
    del obj['sync_deleted']


class ApiTest(APITestCase):
    ''' Teste das chamdas da API '''

    def setUp(self):
        create_or_update_groups()
        # Criar o agente e autenticar-se
        self.agente = AgenteFactory(cpf=12345678909,
                                    municipio=MunicipioFactory())
        self.client.login(cpf=12345678909, password='dummy')
        # Criar quadras e associá-las ao agente
        self.bairro = BairroFactory.create(municipio=self.agente.municipio)
        # criar imovel e trabalho para o agente
        self.imovel = ImovelFactory()
        self.trabalho = TrabalhoFactory(
            agente=self.agente, quadra=self.imovel.lado.quadra)

    def test_adicionar_quadra(self):
        ''' Adicionar um nova quadra '''

        quadra = QuadraFactory.build(bairro=self.bairro)
        quadra_serializer = serializer_factory(Quadra)
        request_data = quadra_serializer(quadra).data
        adicionar_sync_state(request_data)

        # fazer requisição a API
        url = reverse('api:quadras')
        response = self.client.post(url, [request_data], format='json')
        self.assertEqual(response.data, {'status': 'ok'})

        # testar se os dados foram atuliazados
        self.assertEqual(
            model_to_dict(quadra),
            model_to_dict(Quadra.objects.get(id=quadra.id))
        )

    def test_atualizar_quadra(self):
        ''' Atualizar uma quadra já existente '''

        # criar quadra e associar ao agente
        quadra = QuadraFactory.create(bairro=self.bairro)
        TrabalhoFactory(agente=self.agente, quadra=quadra)
        quadra_serializer = serializer_factory(Quadra)
        request_data = quadra_serializer(quadra).data
        adicionar_sync_state(request_data)

        # fazer requisição a API
        url = reverse('api:quadras')
        response = self.client.post(url, [request_data], format='json')
        self.assertEqual(response.data, {'status': 'ok'})

        # testar se os dados foram atuliazados
        self.assertEqual(
            model_to_dict(quadra),
            model_to_dict(Quadra.objects.get(id=quadra.id))
        )

    def test_adicionar_lado(self):
        ''' Adicionar um lado de quadra e logradouro relacionado '''

        # criar quadra e associar ao agente
        self.quadra = QuadraFactory(bairro=self.bairro)
        TrabalhoFactory(agente=self.agente, quadra=self.quadra)

        # Criar objeto logradouro transiente
        logradouro = LogradouroFactory.build(
            id=str(uuid()), municipio=self.quadra.bairro.municipio)
        rua_serializer = serializer_factory(Logradouro)
        request_data = rua_serializer(logradouro).data
        adicionar_sync_state(request_data)

        # fazer requisição a API
        url = reverse('api:logradouros')
        response = self.client.post(url, [request_data], format='json')
        self.assertEqual(response.data, {'status': 'ok'})

        # testar se os dados foram atuliazados
        self.assertEqual(
            model_to_dict(logradouro),
            model_to_dict(Logradouro.objects.get(id=logradouro.id))
        )

        # Criar objeto lado transiente
        lado = LadoFactory.build(id=uuid(), logradouro=logradouro,
                                 quadra=self.quadra)
        lado_serializer = serializer_factory(LadoQuadra)
        request_data = lado_serializer(lado).data
        adicionar_sync_state(request_data)

        # fazer requisição a API
        url = reverse('api:lados')
        response = self.client.post(url, [request_data], format='json')
        self.assertEqual(response.data, {'status': 'ok'})

        # testar se os dados foram atuliazados
        self.assertEqual(
            model_to_dict(lado),
            model_to_dict(LadoQuadra.objects.get(id=lado.id))
        )

    def test_adicionar_visita(self):
        ''' Adicionar nova visita ao ciclo atual '''

        # Criar objeto visita transiente
        visita = VisitaFactory.build(id=uuid(), imovel=self.imovel,
                                     agente=self.agente,
                                     ciclo=self.trabalho.ciclo)
        serializer = serializer_factory(Visita)
        request_data = serializer(visita).data
        adicionar_sync_state(request_data)

        # fazer requisição a API
        url = reverse('api:visitas')
        response = self.client.post(url, [request_data], format='json')
        self.assertEqual(response.data, {'status': 'ok'})

        # testar se os dados foram inseridos
        self.assertEqual(
            model_to_dict(visita),
            model_to_dict(Visita.objects.get(id=visita.id))
        )

    def test_adicionar_imovel_raw(self):
        lado = LadoFactory()
        imovel_json = '''[{
            "numero":"007","id":"1076acde-944b-4469-8f23-951338f9646b",
            "lado":"%(lado)s","tipo":1,"ordem":0,
            "habitantes":0,"gatos":0,"status":0,"caes":0,
            "sync_version":"","sync_changed":"2015-03-01T23:53:29.941",
            "sync_deleted":false}]''' % {'lado': lado.id}
        url = reverse('api:imoveis')
        response = self.client.post(url, imovel_json, content_type='application/json')
        self.assertEqual(response.data, {'status': 'ok'})
        self.assertIsNotNone(Imovel.objects.get(id='1076acde-944b-4469-8f23-951338f9646b'))

    def test_adicionar_visita_raw(self):
        imovel = ImovelFactory()
        visita_json = '''[{
            "agente":"%(agente)s",
            "tipo":1,
            "pendencia":1,
            "larvicida":"vl",
            "imovel":"%(imovel)s",
            "data":"2015-02-23",
            "hora":"17:24:22.000000",
            "C":0, "E":0, "A1":0,
            "depositos_tratados":4,
            "depositos_eliminados":7,
            "imovel_inspecionado":false,
            "imovel_tratado":true,
            "A2":0, "D2":0, "B":0,
            "amostra_inicial":0,
            "qtd_larvicida":4.0,
            "amostra_final":0,
            "D1":0,
            "tubitos":0,
            "ciclo":"%(ciclo)s",
            "id":"2655c7ae-3505-41c1-a3e6-a738d25915c0",
            "sync_version":"", "sync_deleted":false,
            "sync_changed":"2015-03-01T23:53:29.941"}]
        ''' % {
            'agente': self.agente.id,
            'imovel': imovel.id,
            'ciclo': self.trabalho.ciclo.id
        }

        url = reverse('api:visitas')
        response = self.client.post(url, visita_json, content_type='application/json')
        self.assertEqual(response.data, {'status': 'ok'})
        self.assertIsNotNone(Visita.objects.get(id='2655c7ae-3505-41c1-a3e6-a738d25915c0'))


class SyncTest(APITestCase):
    ''' Teste de sincronização '''

    def setUp(self):
        create_or_update_groups()
        # Criar o agente e autenticar-se
        self.agente = AgenteFactory(cpf=12345678909,
                                    municipio=MunicipioFactory())
        self.client.login(cpf=12345678909, password='dummy')
        self.since = datetime.now() - timedelta(minutes=1)
        self.lado = LadoFactory()
        self.trabalho = TrabalhoFactory(
            agente=self.agente, quadra=self.lado.quadra)
        self.imoveis = ImovelFactory.create_batch(10, lado=self.lado)

    def test_sincronizar_imoveis(self):
        sync_imovel_serializer = sync_serializer_factory(Imovel)
        imovel_serializer = serializer_factory(Imovel)
        alterar_imoveis = sync_imovel_serializer(
            random.sample(self.imoveis, 5), many=True).data
        novos_imoveis = imovel_serializer(
            ImovelFactory.build_batch(5, lado=self.lado), many=True).data
        novos_imoveis = [adicionar_sync_state(x) for x in novos_imoveis]
        request_data = alterar_imoveis + novos_imoveis
        #print request_data
        url = "{0}?from={1}".format(reverse('api:imoveis'),
                                    self.since.isoformat())
        response = self.client.post(url, request_data, format='json')
        request_ids = set([d['id'] for d in request_data])
        response_ids = set([d['id'] for d in response.data])
        self.assertTrue(request_ids.issubset(response_ids))

    def test_remover_imovel(self):
        sync_imovel_serializer = sync_serializer_factory(Imovel)
        request_data = sync_imovel_serializer(
            random.sample(self.imoveis, 2), many=True).data
        for imovel in request_data:
            imovel['sync_deleted'] = True
        url = "{0}?from={1}".format(reverse('api:imoveis'),
                                    self.since.isoformat())
        response = self.client.post(url, request_data, format='json')
        remover_imoveis = set([d['id'] for d in request_data])
        imoveis_removidos = set(
            [d['id'] for d in response.data if d['sync_deleted']])
        self.assertEqual(remover_imoveis, imoveis_removidos)
