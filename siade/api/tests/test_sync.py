# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from uuid import uuid4 as uuid
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_sync.serializers import sync_serializer_factory
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


class SyncTest(APITestCase):
    ''' Teste de sincronização '''

    def setUp(self):
        create_or_update_groups()
        # Criar o agente e autenticar-se
        self.agente = AgenteFactory(cpf=12345678909,
                                    municipio=MunicipioFactory())
        self.client.login(cpf=12345678909, password='dummy'),
        # Criar quadras e associá-las ao agente
        self.bairro = BairroFactory.create(municipio=self.agente.municipio)

    def test_atualizar_quadra(self):
        ''' Atualizar uma quadra já existente '''

        # criar quadra e associar ao agente
        quadra = QuadraFactory.create(bairro=self.bairro)
        TrabalhoFactory(agente=self.agente, quadra=quadra)

        # enviar dados
        quadra_serializer = sync_serializer_factory(Quadra)
        request_data = quadra_serializer([quadra]).data
        url = reverse('api:quadras')
        response = self.client.post(url, request_data, format='json')
        self.assertEqual(response.status_code, 200)

        # Remover dados desncessários e comparar resultados
        response_data = response.data
        for i in request_data + response_data:
            del i['sync_version'], i['sync_changed']
        self.assertEqual(request_data, response_data)

    def est_adicionar_lado(self):
        ''' Adicionar um lado de quadra e logradouro relacionado '''

        # criar quadra e associar ao agente
        self.quadra = QuadraFactory.create(bairro=self.bairro)
        TrabalhoFactory(agente=self.agente, quadra=self.quadra)

        # Criar objeto logradouro transiente
        logradouro = LogradouroFactory.build(
            id=uuid(), municipio=self.quadra.bairro.municipio)
        rua_serializer = serializer_factory(Logradouro)
        request_data = rua_serializer(logradouro).data
        adicionar_sync_state(request_data)

        # fazer requisição a API
        url = reverse('api:logradouros')
        response = self.client.post(url, [request_data], format='json')
        self.assertEqual(response.status_code, 200)

        # Remover dados desncessários e comparar resultados
        response_data = response.data[0]
        for i in [request_data, response_data]:
            del i['sync_version'], i['sync_changed']
        self.assertEqual(request_data, response_data)

        # Criar objeto lado transiente
        lado = LadoFactory.build(id=uuid(), logradouro=logradouro,
                                 quadra=self.quadra)
        lado_serializer = serializer_factory(LadoQuadra)
        request_data = lado_serializer(lado).data
        adicionar_sync_state(request_data)

        # fazer requisição a API
        url = reverse('api:lados')
        response = self.client.post(url, [request_data], format='json')
        self.assertEqual(response.status_code, 200)

        # Remover dados desncessários e comparar resultados
        response_data = response.data[0]
        for i in [request_data, response_data]:
            del i['sync_version'], i['sync_changed']
        self.assertEqual(request_data, response_data)


class VisitasTest(APITestCase):
    def setUp(self):
        create_or_update_groups()
        # Criar o agente e autenticar-se
        self.agente = AgenteFactory(cpf=12345678909,
                                    municipio=MunicipioFactory())
        self.client.login(cpf=12345678909, password='dummy'),
        # criar imovel e trabalho para o agente
        self.imovel = ImovelFactory()
        self.trabalho = TrabalhoFactory(
            agente=self.agente, quadra=self.imovel.lado.quadra)

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
        self.assertEqual(response.status_code, 200)

        # Remover dados desncessários e comparar resultados
        response_data = response.data[0]
        for i in [request_data, response_data]:
            del i['sync_version'], i['sync_changed']
        self.assertEqual(request_data, response_data)
