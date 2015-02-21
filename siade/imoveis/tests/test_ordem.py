# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .factories import LadoFactory, ImovelFactory
from ..models import Imovel


class ImovelTest(TestCase):
    def setUp(self):
        # criar registros necessários para se adicionar um imovel
        self.lado = LadoFactory()
        ImovelFactory.create_batch(20, lado=self.lado)

    def test_ordem_imovel(self):
        ''' Ordem de imoveis se mantém ao adicionar '''
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))

    def test_adicionar_imovel(self):
        ''' Ordem de imoveis se mantém ao adicionar no meio '''
        # Adcionar alguns imoveis no meio
        self.lado.imoveis.create(numero=3, habitantes=1, ordem=3)
        Imovel(lado=self.lado, numero=3, habitantes=1, ordem=12).save()
        # testar se foi inserido corretamente
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))

    def test_remover_imovel(self):
        '''Ordem de imoveis se mantém ao remover '''
        self.lado.imoveis.get(ordem=7).delete()
        self.lado.imoveis.get(ordem=12).delete()
        self.lado.imoveis.get(ordem=1).delete()
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))

    def test_atualizar_imovel(self):
        ''' Ordem de imoveis se mantém ao atualizar '''
        imovel = self.lado.imoveis.get(ordem=15)
        imovel.habitantes = 3
        imovel.save()
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))

    def test_alterar_ordem_imovel(self):
        ''' Mudar numero de ordem imoveis mantem a sequencia '''
        imovel = self.lado.imoveis.get(ordem=15)
        imovel.ordem = 3
        imovel.save()
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))
