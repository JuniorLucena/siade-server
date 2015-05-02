from uuid import uuid4 as uuid
import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from ..models import (UF, Municipio, Bairro, Logradouro, Quadra,
                      LadoQuadra, Imovel)


class UFFactory(DjangoModelFactory):
    nome = 'Rio Grande do Norte'
    sigla = 'RN'

    class Meta:
        model = UF
        django_get_or_create = ('nome',)


class MunicipioFactory(DjangoModelFactory):
    nome = factory.Sequence(lambda n: 'Municipio {0}'.format(n))
    uf = factory.SubFactory(UFFactory)
    codigo = factory.Sequence(lambda n: n)

    class Meta:
        model = Municipio
        django_get_or_create = ('nome',)


class BairroFactory(DjangoModelFactory):
    nome = factory.Sequence(lambda n: 'Bairro {0}'.format(n))
    municipio = factory.SubFactory(MunicipioFactory)
    codigo = factory.Sequence(lambda n: n)

    class Meta:
        model = Bairro
        django_get_or_create = ('nome', 'municipio')


class LogradouroFactory(DjangoModelFactory):
    nome = factory.Sequence(lambda n: 'Rua Projetada {0}'.format(n))
    municipio = factory.SubFactory(MunicipioFactory)

    @factory.lazy_attribute
    def id(self):
        return str(uuid())

    class Meta:
        model = Logradouro
        django_get_or_create = ('nome', 'municipio')


class QuadraFactory(DjangoModelFactory):
    numero = factory.Sequence(lambda n: n)
    bairro = factory.SubFactory(BairroFactory)

    @factory.lazy_attribute
    def id(self):
        return str(uuid())

    class Meta:
        model = Quadra
        django_get_or_create = ('bairro', 'numero')


class LadoFactory(DjangoModelFactory):
    numero = factory.Sequence(lambda n: n)
    quadra = factory.SubFactory(QuadraFactory)
    logradouro = factory.SubFactory(LogradouroFactory)

    @factory.lazy_attribute
    def id(self):
        return str(uuid())

    class Meta:
        model = LadoQuadra
        django_get_or_create = ('quadra', 'numero')


class ImovelFactory(DjangoModelFactory):
    lado = factory.SubFactory(LadoFactory)
    ordem = factory.Sequence(lambda n: n)
    numero = factory.fuzzy.FuzzyInteger(1, 8000)
    tipo = factory.fuzzy.FuzzyChoice(Imovel.Tipo.values.keys())
    habitantes = factory.fuzzy.FuzzyInteger(0, 10)
    caes = factory.fuzzy.FuzzyInteger(0, 5)
    gatos = factory.fuzzy.FuzzyInteger(0, 5)
    ponto_estrategico = factory.fuzzy.FuzzyChoice((True, False))

    @factory.lazy_attribute
    def id(self):
        return str(uuid())

    class Meta:
        model = Imovel
        django_get_or_create = ('lado', 'numero')
