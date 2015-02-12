# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.db.models.loading import get_model
from rest_framework.test import APITestCase
from siade.agentes.models import Agente

class ImoveisTest(APITestCase):
    def setUp(self):
        self.user = Agente.objects.create(
            cpf=12345678909, nome='Test', sobrenome='User',
            password='testing'
        )
        
        uf = UF.objects.create(nome='Rio Grande do Norte', sigla='RN')
        municipio = Municipio.objects.create('Pau dos Ferros', uf=uf)
        bairro = Bairro.objects.create('Centro', municipio=municipio)