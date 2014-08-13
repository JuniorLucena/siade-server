# -*- coding: utf-8 -*-
from datetime import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.db.models.loading import get_model
from rest_framework.test import APITestCase
from simple_history.models import HistoricalRecords


class SycTest(APITestCase):
    def setUp(self):
        self.url = reverse('rest-synchro')
        # autenticar-se
        User = get_user_model()
        self.user = User.objects.create_superuser(
            'testuser', email='testuser@test.com', password='testing'
        )
        self.client.login(username='testuser', password='testing')
        # definir usuário para o django-simple-history
        HistoricalRecords.thread._history_user = self.user
        # criar models principais
        UF = get_model('imoveis', 'UF')
        self.uf = UF(nome='UF1')
        self.uf._history_user = self.user
        self.uf.save()

        Municipio = get_model('imoveis', 'Municipio')
        self.municipio = Municipio(nome='Mun1', uf=self.uf)
        self.municipio._history_user = self.user
        self.municipio.save()

        Bairro = get_model('imoveis', 'Bairro')
        self.bairro = Bairro(nome='B1', municipio=self.municipio)
        self.bairro._history_user = self.user
        self.bairro.save()

    def test_get_no_params(self):
        REST_SYNC_MODELS = getattr(settings, 'REST_SYNC_MODELS', [])
        data = {k: [] for k in REST_SYNC_MODELS}
        response = self.client.get(self.url)
        self.assertEqual(response.data, data)

    def test_sync_new(self):
        data = {
            'imoveis.Quadra': [
                {
                    'id': 2,
                    'bairro': self.bairro.id,
                    'numero': '1A',
                    'sync_changed': '2014-08-07T20:18:07.147',
                    'sync_version': None,
                    'sync_deleted': 0,
                }
            ]
        }
        response = self.client.post(self.url, data, format='json')

    def test_sync_existing(self):
        data = {
            'imoveis.Quadra': [
                {
                    'id': 2,
                    'bairro': self.bairro.id,
                    'numero': '1A',
                    'sync_changed': '2014-08-07T20:18:07.147',
                    'sync_version': 1,
                    'sync_deleted': 0,
                }
            ]
        }
        response = self.client.post(self.url, data, format='json')
