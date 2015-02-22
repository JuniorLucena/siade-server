# -*- coding: utf-8 -*-
'''
Gerar dados ficticios de ciclos
'''
import logging
from math import ceil
from random import randint, random, choice
from datetime import date, timedelta
from itertools import cycle
from siade.imoveis.models import *
from siade.trabalhos.models import *
from faker import Factory
faker = Factory.create('pt_BR')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def gerar_ciclo(numero, ano_base, data_inicio, fechado=True):
    '''Gerar um ciclo'''
    print 'Ciclo %d/%d (%s)' % (numero, ano_base, data_inicio)
    atividade = choice(Ciclo.Atividade.values.keys())
    data_fim = data_inicio + timedelta(days=randint(50, 70))
    ciclo = Ciclo.objects.create(
        data_inicio=data_inicio,
        data_fim=data_fim,
        numero=numero,
        ano_base=ano_base,
        atividade=atividade,
        fechado_em=data_fim
    )
    gerar_trabalhos(ciclo)
    return ciclo


def gerar_ciclos(qtd, ano_base):
    '''Gerar ciclos para um ano'''
    data_inicio = date(ano_base, 1, 5) + timedelta(days=randint(5, 7))
    for i in range(qtd):
        ciclo = gerar_ciclo(i + 1, ano_base, data_inicio)
        data_inicio = ciclo.data_inicio + timedelta(days=randint(5, 10))


def gerar_trabalhos(ciclo):
    quadras_count = Quadra.objects.count()
    agentes_count = Agente.objects.filter(tipo=Agente.Tipo.AgenteCampo).count()
    quadras_por_agente = int(ceil(float(quadras_count) / agentes_count))
    quadras = iter(Quadra.objects.all())
    for agente in Agente.objects.filter(tipo=Agente.Tipo.AgenteCampo):
        for i in range(quadras_por_agente):
            try:
                quadra = next(quadras)
                print '* Trabalho A.%s Q.%s C.%s' % (agente, quadra, ciclo)
                trabalho = Trabalho.objects.create(agente=agente,
                                                   quadra=quadra,
                                                   ciclo=ciclo)
                # Gerar visitas para este trabalho
                if ciclo.fechado_em:
                    gerar_visitas(trabalho, 100)
                else:
                    gerar_visitas(trabalho, randint(0, 100))
            except StopIteration:
                break


def gerar_visita(ciclo, agente, imovel):
    print '  * Visita em %s por %s' % (imovel, agente)
    datahora_visita = faker.date_time_between(
        ciclo.data_inicio, ciclo.data_fim)
    Visita.objects.create(
        data=datahora_visita.date(),
        hora=datahora_visita.time(),
        ciclo=ciclo,
        agente=agente,
        imovel=imovel,
        pendencia=0
    )


def gerar_visitas(trabalho, percentual=100):
    imoveis = Imovel.objects.filter(lado__quadra=trabalho.quadra)
    total_imoveis = imoveis.count()
    total_visitas = total_imoveis * percentual/100
    for imovel in imoveis[:total_visitas]:
        gerar_visita(trabalho.ciclo, trabalho.agente, imovel)


def run(qtd=3, ano=2014):
    qtd, ano = int(qtd), int(ano)
    Ciclo.objects.all().delete()
    Trabalho.objects.all().delete()
    Visita.objects.all().delete()
    gerar_ciclos(qtd, ano)
