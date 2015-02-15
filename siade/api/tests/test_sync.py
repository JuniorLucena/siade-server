# -*- coding: utf-8 -*-
from datetime import datetime
from shortuuid import uuid
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_sync.serializers import sync_serializer_factory
from siade.imoveis.models import Quadra
from siade.api.serializers import serializer_factory
from siade.imoveis.tests.factories import (BairroFactory, QuadraFactory,
                                           ImovelFactory)
from siade.trabalhos.tests.factories import TrabalhoFactory


class SyncTest(APITestCase):
    ''' Teste de sincronização '''
    def setUp(self):
        # Criar o agente e autenticar-se
        User = get_user_model()
        self.agente = User.objects.create_superuser(
            cpf=12345678909, nome='Test', sobrenome='User',
            password='testing'
        )
        self.client.login(cpf=12345678909, password='testing')
        # Criar quadras e associá-las ao agente
        self.bairro = BairroFactory.create()

    def test_atualizar_quadra(self):
        ''' Atualizar uma quadra já existente '''
        # criar quadra e associar ao agente
        quadra = QuadraFactory.create(bairro=self.bairro)
        TrabalhoFactory(agente=self.agente, quadra=quadra)
        # enviar dados
        serializer = sync_serializer_factory(Quadra)
        request_data = serializer([quadra]).data
        url = reverse('api:quadras')
        response = self.client.post(url, request_data, format='json')
        response_data = response.data
        # ignorar dados que sempre mudam
        for i in request_data + response_data:
            del i['sync_version'], i['sync_changed']

        self.assertEqual(request_data, response_data)
