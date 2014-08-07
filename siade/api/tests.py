from json import dumps, loads
from django.core.urlresolvers import reverse
#from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


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
