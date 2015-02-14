from datetime import date, timedelta
from random import randint
import factory
from factory.django import DjangoModelFactory
from ..models import Ciclo, Trabalho


class CicloFactory(DjangoModelFactory):
    data_inicio = factory.fuzzy.FuzzyDate(date(2014, 1, 1), date(2014, 10, 1))
    numero = factory.Sequence(lambda n: n)
    ano_base = 2014

    @factory.LazyAttribute
    def data_fim(self):
        return self.data_inicio + timedelta(days=randint(30, 60))

    class Meta:
        model = Ciclo


class TrabalhoFactory(DjangoModelFactory):
    ciclo = factory.SubFactory(CicloFactory)

    class Meta:
        model = Trabalho
