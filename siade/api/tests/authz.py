# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.db.models.loading import get_model
from rest_framework.test import APITestCase


class AuthzTest(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_superuser(
            cpf=12345678909, nome='Test', sobrenome='User',
            password='testing'
        )

    def _doLogin(self):
        self.client.login(cpf=12345678909, password='testing')

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
