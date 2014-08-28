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

    def test_sync_new_quadra(self):
        self.url = reverse('rest-synchro', kwargs={
            'app': 'imoveis', 'model': 'Quadra',
        })
        data = [{
            'id': 2,
            'bairro': self.bairro.id,
            'numero': '1A',
            'sync_changed': '2014-08-07T20:18:07.147',
            'sync_version': None,
            'sync_deleted': False,
        }, {
            'id': 3,
            'bairro': self.bairro.id,
            'numero': '4',
            'sync_changed': '2014-08-12T20:18:07.147',
            'sync_version': 1,
            'sync_deleted': False,
        }]
        self.client.post(self.url, data, format='json')
        response = self.client.get(self.url)
        # pegar a quadra salva
        posted = data[0]
        saved = response.data[0]
        # remover dados que sempre mudam
        posted['id'] = saved['id']
        posted['sync_version'] = saved['sync_version']
        posted['sync_changed'] = saved['sync_changed']
        self.assertEqual(posted, saved)

    def test_sync_existing_quadra(self):
        self.url = reverse('rest-synchro', kwargs={
            'app': 'imoveis', 'model': 'Quadra',
        })
        data = [{
            'id': 1,
            'bairro': self.bairro.id,
            'numero': '2A',
            'sync_changed': '2014-08-07T20:18:07.147',
            'sync_version': 1,
            'sync_deleted': False,
        }, {
            'id': 3,
            'bairro': self.bairro.id,
            'numero': '4',
            'sync_changed': '2014-08-12T20:18:07.147',
            'sync_version': 1,
            'sync_deleted': False,
        }]
        self.client.post(self.url, data, format='json')
        response = self.client.get(self.url)
        # pegar a quadra salva
        posted = data[0]
        saved = response.data[0]
        # remover dados que sempre mudam
        posted['id'] = saved['id']
        posted['sync_version'] = saved['sync_version']
        posted['sync_changed'] = saved['sync_changed']
        self.assertEqual(posted, saved)

    def test_sync_raw_data(self):
        self.url = reverse('rest-synchro', kwargs={
            'app': 'imoveis', 'model': 'Logradouro',
        })
        data = '''[{
            "municipio":1,
            "nome":"Independencia",
            "id":1,
            "sync_changed":"2014-08-14T18:04:25.968",
            "sync_deleted":false,
            "sync_version":4
        },{
            "municipio":1,
            "nome":"Abiorama",
            "id":2,
            "sync_changed":"2014-08-14T18:04:25.968",
            "sync_deleted":false,
            "sync_version":3
        },{
            "municipio":1,
            "nome":"13 de maio",
            "id":4,"sync_changed":"2014-08-14T18:04:25.968",
            "sync_deleted":false,"sync_version":1
        },{
            "municipio":1,
            "nome":"13 de maio",
            "id":5,
            "sync_changed":"2014-08-14T18:04:25.968",
            "sync_deleted":false,"sync_version":2
        },{
            "municipio":1,
            "nome":"Nova rua",
            "id":6,"sync_changed":"2014-08-14T18:04:25.968",
            "sync_deleted":false,
            "sync_version":5
        },{
            "municipio":1,
            "nome":"Nova rua",
            "id":7,
            "sync_changed":"2014-08-14T18:04:25.968",
            "sync_deleted":false,
            "sync_version":6
        }]'''
        self.client.post(self.url, data, content_type='application/json')
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 6)
