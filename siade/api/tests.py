# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.db.models.loading import get_model
from rest_framework.test import APITestCase
from siade.api.sync.serializers import SyncSerializerForModel


class ApiTest(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_superuser(
            'testuser',
            email='testuser@test.com',
            password='testing'
        )

    def _doLogin(self):
        self.client.login(username='testuser', password='testing')

    def test_adicionar_uf_sem_autenticar(self):
        uflist = reverse('uf-list')
        response = self.client.post(uflist, {
            'nome': 'Rio Grande do Norte',
            'sigla': 'RN'
        }, format='json')
        self.assertEqual(response.data, {
            'detail': 'Authentication credentials were not provided.'
        })

    def test_adicionar_uf_autenticado(self):
        self._doLogin()
        url = reverse('uf-list')
        data = {
            'nome': 'Rio Grande do Norte',
            'sigla': 'RN'
        }
        response = self.client.post(url, data, format='json')
        data['id'] = response.data['id']
        self.assertEqual(data, response.data)

    def test_sync_serializer(self):
        self._doLogin()
        # Criar um registro
        url = reverse('logradouro-list')
        data = {'nome': 'Rua Jose Pinheiro'}
        response = self.client.post(url, data, format='json')
        Logradouro = get_model('imoveis', 'Logradouro')
        o = Logradouro.objects.get(pk=response.data['id'])
        oh = o.history.first()
        # serialize
        serializer = SyncSerializerForModel(Logradouro)
        data = serializer(o).data
        # faz os testes
        self.assertEqual(data['nome'], o.nome)
        self.assertEqual(data['municipio'], o.municipio)
        self.assertEqual(data['sync_changed'], oh.history_date)
        self.assertEqual(data['sync_version'], oh.history_id)
        self.assertEqual(data['sync_deleted'], False)
