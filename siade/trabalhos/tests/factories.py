from __future__ import unicode_literals
from datetime import datetime, date, timedelta
from time import time
from random import randint
from shortuuid import uuid
import factory
from factory.django import DjangoModelFactory
from siade.agentes.tests.factories import AgenteFactory
from siade.imoveis.tests.factories import ImovelFactory
from ..models import Ciclo, Trabalho, Visita


class CicloFactory(DjangoModelFactory):
    id = uuid()
    data_inicio = factory.fuzzy.FuzzyDate(date(2014, 1, 1), date(2014, 10, 1))
    numero = 1
    ano_base = 2014
    atividade = factory.fuzzy.FuzzyChoice(Ciclo.Atividade.values.keys())

    @factory.LazyAttribute
    def data_fim(self):
        return self.data_inicio + timedelta(days=randint(30, 60))

    class Meta:
        model = Ciclo
        django_get_or_create = ('numero', 'ano_base')


class TrabalhoFactory(DjangoModelFactory):
    id = uuid()
    ciclo = factory.SubFactory(CicloFactory)

    class Meta:
        model = Trabalho


class VisitaFactory(DjangoModelFactory):
    data = date.today()
    hora = datetime.fromtimestamp(round(time(), 3)).time()
    ciclo = factory.SubFactory(CicloFactory)
    agente = factory.SubFactory(AgenteFactory)
    imovel = factory.SubFactory(ImovelFactory)
    tipo = Visita.Tipo.Normal
    pendencia = Visita.Pendencia.Nenhuma
    imovel_tratado = False
    imovel_inspecionado = False
    larvicida = ''

    class Meta:
        model = Visita
