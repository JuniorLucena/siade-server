# -*- coding: utf-8 -*-
'''
Gerar dados ficticios de trabalhos
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

trabalho_atividades = (
    ('Tratamento', 'T'),
    ('Levantamento de índice', 'LI'),
    ('Levantamento de índice + Tratamento', 'LI+T'),
)

def gerar_ciclo(numero, ano_base, data_inicio):
    '''Gerar um ciclo'''
    ciclo = Ciclo.objects.create(
        data_inicio=data_inicio,
        data_fim=data_inicio + timedelta(days=randint(50, 70)),
        numero=numero,
        ano_base=ano_base
    )
    logger.debug('Ciclo %d/%d (%s)', numero, ano_base, data_inicio)
    return ciclo


def gerar_ciclos(ano_base):
    '''Gerar ciclos para um ano'''
    data_inicio = date(ano_base, 1, 1) + timedelta(days=randint(5, 7))
    for i in range(5):
        ciclo = gerar_ciclo(i + 1, ano_base, data_inicio)
        data_inicio = ciclo.data_inicio + timedelta(days=randint(5, 10))


def gerar_trabalhos(ciclo):
    quadras_count = Quadra.objects.count()
    agentes_count = Agente.objects.filter(nivel=1).count()
    quadras_por_agente = int(ceil(float(quadras_count) / agentes_count))
    quadras = iter(Quadra.objects.all())
    for agente in Agente.objects.filter(nivel=1):
        for i in range(quadras_por_agente):
            try:
                quadra = next(quadras)
                logger.debug('Trabalho C.%s Q.%s A.%s', agente, quadra, ciclo)
                trabalho = Trabalho.objects.create(agente=agente,
                                                   quadra=quadra,
                                                   ciclo=ciclo)
            except StopIteration:
                break


def gerar_visita(ciclo, agente, imovel):
    logger.debug('Visita %s (ciclo %s)', imovel, ciclo)
    datahora_visita = faker.date_time_between(
        ciclo.data_inicio, ciclo.data_fim)
    nome, sigla = choice(trabalho_atividades)
    atividade, c = Atividade.objects.get_or_create(nome=nome, sigla=sigla)
    return Visita.objects.create(
        data=datahora_visita.date(),
        hora=datahora_visita.time(),
        ciclo=ciclo,
        agente=agente,
        imovel=imovel,
        atividade=atividade
    )


def gerar_visitas(ciclo):
    for trabalho in Trabalho.objects.all():
        for imovel in Imovel.objects.filter(lado__quadra=trabalho.quadra):
            gerar_visita(trabalho.ciclo, trabalho.agente, imovel)


def run():
    Ciclo.objects.all().delete()
    Trabalho.objects.all().delete()
    Visita.objects.all().delete()
    gerar_ciclos(2013)
    ciclos = Ciclo.objects.all()
    for ciclo in ciclos:
        gerar_trabalhos(ciclo)
    gerar_visitas(ciclo)
