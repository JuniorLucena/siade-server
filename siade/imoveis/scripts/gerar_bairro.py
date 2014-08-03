# -*- coding: utf-8 -*-
'''
Gerar dados ficticios de um bairro
'''
from random import randint
from siade.imoveis.models import *
from .dados import Gerador


class Gerador_de_bairro(Gerador):
    def __init__(self, municipio=None):
        self.municipio = municipio or self.gerar_municipio()
        bairro, c = Bairro.objects.get_or_create(
            nome=Gerador.gerar_bairro_nome(self),
            municipio=self.municipio
        )
        self.bairro = bairro

    def gerar_uf(self):
        sigla, nome = Gerador.gerar_uf(self)
        uf, c = UF.objects.get_or_create(sigla=sigla, nome=nome)
        return uf

    def gerar_municipio(self, uf=None):
        mu, c = Municipio.objects.get_or_create(
            nome=Gerador.gerar_municipio(self), uf=uf or self.gerar_uf())
        return mu

    def gerar_rua(self):
        return Logradouro.objects.create(
            nome=Gerador.gerar_rua(self), municipio=self.municipio)

    def gerar_lado_quadra(self, logradouro, qtd_imoveis, numero=1):
        imoveis = self.gerar_imoveis(qtd_imoveis)
        lado = LadoQuadra(logradouro=logradouro, numero=numero)
        lado.imoveis_list = imoveis
        from pprint import pprint
        print numero, qtd_imoveis
        return lado

    def gerar_quadra(self, numero, lados, pontos=None):
        quadra = Quadra(numero=numero)
        quadra.lados_list = lados
        return quadra

    def gerar_imovel(self, ordem=0, numero=None):
        imovel = Gerador.gerar_imovel(self, ordem, numero)
        tipo_nome, tipo_sigla = imovel['tipo']
        tipo, created = TipoImovel.objects.get_or_create(
            nome=tipo_nome, sigla=tipo_sigla)
        imovel['tipo'] = tipo
        return Imovel(**imovel)


def run():
    gen = Gerador_de_bairro()
    print 'Gerando dados do bairro'
    quadras = gen.gerar_quadras(randint(4, 8), randint(4, 8))
    print 'Salvando no banco de dados'
    for quadra in quadras:
        quadra.bairro = gen.bairro
        quadra.save()
        for lado in quadra.lados_list:
            lado.quadra = quadra
            lado.save()
            for imovel in lado.imoveis_list:
                imovel.lado = lado
                imovel.save()
