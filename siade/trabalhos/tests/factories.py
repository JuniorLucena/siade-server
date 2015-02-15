from datetime import date, timedelta
from random import randint
from shortuuid import uuid
import factory
from factory.django import DjangoModelFactory
from ..models import Ciclo, Trabalho


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
