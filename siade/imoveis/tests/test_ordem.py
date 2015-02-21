# -*- coding: utf-8 -*-
from django.test import TestCase
from ..models import UF, Municipio, Bairro, Quadra, Logradouro, Imovel


class ImovelTest(TestCase):
    def setUp(self):
        # criar registros necessários para se adicionar um imovel
        uf = UF.objects.create(nome='Rio Grande do Norte', sigla='RN')
        municipio = Municipio.objects.create(nome='Pau dos Ferros', uf=uf)
        bairro = Bairro.objects.create(nome='Centro', municipio=municipio)
        quadra = Quadra.objects.create(numero=1, bairro=bairro)
        logradouro = Logradouro.objects.create(nome='Centro',
                                               municipio=municipio)
        self.lado = quadra.lados.create(numero=1, logradouro=logradouro)
        # Criar lista de imóveis
        for i in range(20):
            self.lado.imoveis.create(numero=1, habitantes=1)

    def test_ordem_imovel(self):
        '''Foi inserido corretamente'''
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))

    def test_adicionar_imovel(self):
        '''Adicionar imoveis mantem a sequencia'''
        # Adcionar alguns imoveis no meio
        self.lado.imoveis.create(numero=3, habitantes=1, ordem=3)
        Imovel(lado=self.lado, numero=3, habitantes=1, ordem=12).save()
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))

    def test_remover_imovel(self):
        '''Remover imoveis mantem a sequencia'''
        self.lado.imoveis.get(ordem=7).delete()
        self.lado.imoveis.get(ordem=12).delete()
        self.lado.imoveis.get(ordem=1).delete()
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))

    def test_atualizar_imovel(self):
        '''Atualizar imoveis mantem a sequencia'''
        imovel = self.lado.imoveis.get(ordem=15)
        imovel.habitantes = 3
        imovel.save()
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))

    def test_alterar_ordem_imovel(self):
        '''Mudar numero de ordem imoveis mantem a sequencia'''
        imovel = self.lado.imoveis.get(ordem=15)
        imovel.ordem = 3
        imovel.save()
        ordem = [i.ordem for i in self.lado.imoveis.all()]
        total = self.lado.imoveis.count()
        self.assertEqual(ordem, range(1, total+1))
