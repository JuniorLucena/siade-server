# -*- coding: utf-8 -*-
from datetime import datetime
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_sync.serializers import sync_serializer_factory
from siade.agentes.models import Agente
from siade.imoveis.models import Quadra, Logradouro, LadoQuadra
from siade.api.serializers import serializer_factory
from siade.agentes.tests.factories import AgenteFactory
from siade.imoveis.tests.factories import (MunicipioFactory, BairroFactory,
                                           QuadraFactory, LogradouroFactory,
                                           LadoFactory)
from siade.trabalhos.tests.factories import TrabalhoFactory


class SyncTest(APITestCase):
    ''' Teste de sincronização '''
    def adicionar_sync_state(self, obj):
        obj.update({
            'sync_version': '',
            'sync_changed': datetime.now(),
            'sync_deleted': False,
        })
        return obj

    def setUp(self):
        # Criar o agente e autenticar-se
        self.agente = Agente.objects.create_superuser(
            cpf=12345678909, nome='Test', sobrenome='User',
            password='dummy'
        )
        self.agente.municipio = MunicipioFactory()
        self.agente.save()
        #self.agente = AgenteFactory(cpf=12345678909)
        #print self.agente.password
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
        response_data = response.data
        # ignorar dados que sempre mudam
        for i in request_data + response_data:
            del i['sync_version'], i['sync_changed']

        self.assertEqual(request_data, response_data)

    def test_adicionar_logradouro(self):
        # criar quadra e associar ao agente
        self.quadra = QuadraFactory.create(bairro=self.bairro)
        TrabalhoFactory(agente=self.agente, quadra=self.quadra)

        # Adicionar logradouro
        logradouro = LogradouroFactory.build(
            municipio=self.quadra.bairro.municipio)
        rua_serializer = serializer_factory(Logradouro)
        request_data = rua_serializer(logradouro).data
        self.adicionar_sync_state(request_data)
        url = reverse('api:logradouros')
        response = self.client.post(url, [request_data], format='json')
        response_data = response.data[0]
        for i in [request_data, response_data]:
            del i['sync_version'], i['sync_changed']
        self.assertEqual(request_data, response_data)

        # Adicionar lado
        lado = LadoFactory.build(logradouro=logradouro, quadra=self.quadra)
        lado_serializer = serializer_factory(LadoQuadra)
        request_data = lado_serializer(lado).data
        self.adicionar_sync_state(request_data)
        url = reverse('api:lados')
        response = self.client.post(url, [request_data], format='json')
        response_data = response.data[0]
        for i in [request_data, response_data]:
            del i['sync_version'], i['sync_changed']
        self.assertEqual(request_data, response_data)
