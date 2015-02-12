# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.db.models.loading import get_model
from rest_framework.test import APITestCase


class SyncTest(APITestCase):
    ''' Teste de sincronização '''
    def setUp(self):
        # autenticar-se
        User = get_user_model()
        self.user = User.objects.create_superuser(
            cpf=12345678909, nome='Test', sobrenome='User',
            password='testing'
        )
        self.client.login(cpf=12345678909, password='testing')
        # criar models principais
        UF = get_model('imoveis', 'UF')
        self.uf = UF(nome='UF1')
        self.uf.save()

        Municipio = get_model('imoveis', 'Municipio')
        self.municipio = Municipio(nome='Mun1', uf=self.uf)
        self.municipio.save()

        Bairro = get_model('imoveis', 'Bairro')
        self.bairro = Bairro(nome='B1', municipio=self.municipio)
        self.bairro.save()

    def test_sync_new_quadra(self):
        url = '/api/sync/imoveis/quadra/'
        data = [{
            'id': 1,
            'bairro': self.bairro.id,
            'numero': '1',
            'sync_changed': '2014-08-07T20:18:07.147',
            'sync_version': None,
            'sync_deleted': False,
        }]
        self.client.post(url, data, format='json')
        self.client.get(url)

    def test_sync_existing_quadra(self):
        url = '/api/sync/imoveis/quadra/'
        data = [{
            'id': 1,
            'bairro': self.bairro.id,
            'numero': 2,
            'sync_changed': '2014-08-07T20:18:07.147',
            'sync_version': 1,
            'sync_deleted': False,
        }, {
            'id': 3,
            'bairro': self.bairro.id,
            'numero': 4,
            'sync_changed': '2014-08-12T20:18:07.147',
            'sync_version': 1,
            'sync_deleted': False,
        }]
        self.client.post(url, data, format='json')
        response = self.client.get(url)
        # pegar a quadra salva
        posted = data[0]
        saved = response.data[0]
        # remover dados que sempre mudam
        del posted['id'], saved['id']
        del posted['sync_version'], saved['sync_version']
        del posted['sync_changed'], saved['sync_changed']
        self.assertEqual(posted, saved)
