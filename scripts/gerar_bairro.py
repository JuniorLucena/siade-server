# -*- coding: utf-8 -*-
'''
Gerar dados ficticios de um bairro
'''
from random import randint, random
from siade.imoveis.models import *
from faker import Factory
faker = Factory.create('pt_BR')


def weighted_choice(weights):
    '''
    Escolhe aleatoreamente de acordo com os pesos
    '''
    rnd = random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i


def gerar_uf():
    sigla, nome = faker.estado()
    return UF.objects.create(sigla=sigla, nome=nome)


def pegar_municipio(uf=None):
    total_municipio = Municipio.objects.count()
    if total_municipio == 0:
        municipio = Municipio.objects.create(nome=faker.city(),
                                             uf=uf or gerar_uf())
    else:
        total_municipio = randint(0, total_municipio-1)
        municipio = Municipio.objects.all()[total_municipio]
    print 'Municipio: %s, %s' % (municipio.nome, municipio.uf)
    return municipio


def gerar_bairro(municipio, tamanho_x=4, tamanho_y=4):
    print 'Gerando dados de bairro (%d por %d quadras).' % (tamanho_x, tamanho_y)
    bairro = Bairro.objects.create(nome=faker.bairro(), municipio=municipio)
    print '* Bairro: %s' % bairro.nome
    gerar_quadras(bairro, tamanho_x, tamanho_y)
    return bairro


def gerar_rua(municipio):
    nome = 'Rua %s' % faker.name()
    return Logradouro.objects.create(nome=nome, municipio=municipio)


def gerar_lado_quadra(quadra, numero, logradouro, qtd_imoveis):
    print '    * Lado %s, %s, %s' % (numero, logradouro, qtd_imoveis)
    lado = LadoQuadra.objects.create(quadra_id=quadra.pk, numero=numero,
                                     logradouro=logradouro)
    imoveis = gerar_imoveis(lado, qtd_imoveis)
    return lado


def gerar_quadra(bairro, numero, pontos=None):
    print '  * Quadra %s' % numero
    quadra = Quadra.objects.create(numero=numero, bairro=bairro)
    return quadra


def gerar_quadras(bairro, qtd_x, qtd_y):
    ruas = [None] * 4
    quadras = []
    y1 = 0
    for x in range(qtd_x):
        h = weighted_choice((2, 4, 2, 2)) * 2 + 2
        ruas[2] = ruas[2] if x > 0 else gerar_rua(bairro.municipio)
        ruas[0] = gerar_rua(bairro.municipio)

        x1 = 0
        for y in range(qtd_y):
            w = randint(1, 8) * 2 + 4
            pontos = (x1, y1, x1 + w, y1 + h)
            i = len(quadras)
            li = len(quadras) - qtd_y
            ti = len(quadras) - 1
            # rua 0
            if y > 0:
                ruas[0] = ruas[2]
            elif x > 0:
                ruas[0] = quadras[li]['ruas'][0]
            else:
                ruas[0] = gerar_rua(bairro.municipio)
            # rua 1
            if y > 0 and quadras[ti]['pontos'][1] == pontos[1]:
                ruas[1] = quadras[ti]['ruas'][1]
            else:
                ruas[1] = gerar_rua(bairro.municipio)
            # rua 2
            ruas[2] = gerar_rua(bairro.municipio)
            # rua 3
            if x > 0:
                ruas[3] = quadras[li]['ruas'][1]
            elif y > 0:
                ruas[3] = quadras[ti]['ruas'][3]
            else:
                ruas[3] = gerar_rua(bairro.municipio)

            numero = x * qtd_y + abs((qtd_y * (x % 2) - y)) + 1 - (x % 2)
            quadras += [{'pontos': pontos, 'ruas': list(ruas)}]
            tamanhos = [w, h] * 2
            imoveis_numeros = [
                range(x * 20 + 1, (x + 1) * 20 + 1, 2),
                range(y * 10 + 1, (y + 1) * 10 + 1, 2),
                range(x * 20 + 2, (x + 1) * 20 + 2, 2),
                range(y * 10 + 2, (y + 1) * 10 + 2, 2),
            ]
            quadra = gerar_quadra(bairro, numero, pontos)
            for i in range(4):
                gerar_lado_quadra(quadra, i + 1, ruas[i], imoveis_numeros[i])

            x1 += w + 2
        y1 += h + 2


def gerar_imovel(lado, ordem=0, numero=None):
    imovel = Imovel(lado=lado, numero=numero, ordem=ordem,
                    tipo=weighted_choice((0, 3, 3, 1, 2)),
                    habitantes=weighted_choice((0, 2, 3, 3, 2, 1)),
                    caes=weighted_choice((2, 3, 1, 1)),
                    gatos=weighted_choice((2, 3, 1, 1)))

    if imovel.tipo == Imovel.Tipo.Terreno:
        imovel.habitantes = 0

    imovel.save()
    return imovel


def gerar_imoveis(lado, numeros):
    if hasattr(numeros, '__iter__'):
        for i, num in enumerate(numeros):
            gerar_imovel(lado, i + 1, num)
    else:
        for i in range(numeros):
            return gerar_imovel(lado, i + 1)


def run():
    municipio = pegar_municipio()
    bairro = gerar_bairro(municipio, randint(3, 10), randint(4, 10))
    print 'Dados gerados com sucesso.'
