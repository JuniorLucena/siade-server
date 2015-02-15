import factory
import factory.fuzzy
from shortuuid import uuid
from factory.django import DjangoModelFactory
from ..models import (UF, Municipio, Bairro, Logradouro, Quadra,
                      LadoQuadra, Imovel)


class UFFactory(DjangoModelFactory):
    id = uuid()
    nome = factory.Sequence(lambda n: 'UF {0}'.format(n))
    sigla = factory.Sequence(lambda n: '{0}'.format(n))

    class Meta:
        model = UF
        django_get_or_create = ('nome',)


class MunicipioFactory(DjangoModelFactory):
    id = uuid()
    nome = factory.Sequence(lambda n: 'Municipio {0}'.format(n))
    uf = factory.SubFactory(UFFactory)
    codigo = factory.Sequence(lambda n: n)

    class Meta:
        model = Municipio
        django_get_or_create = ('nome',)


class BairroFactory(DjangoModelFactory):
    id = uuid()
    nome = factory.Sequence(lambda n: 'Bairro {0}'.format(n))
    municipio = factory.SubFactory(MunicipioFactory)
    codigo = factory.Sequence(lambda n: n)

    class Meta:
        model = Bairro
        django_get_or_create = ('nome', 'municipio')


class LogradouroFactory(DjangoModelFactory):
    id = uuid()
    nome = factory.Sequence(lambda n: 'Rua Projetada {0}'.format(n))
    municipio = factory.SubFactory(MunicipioFactory)

    class Meta:
        model = Logradouro
        django_get_or_create = ('nome', 'municipio')


class QuadraFactory(DjangoModelFactory):
    id = uuid()
    numero = factory.Sequence(lambda n: n)
    bairro = factory.SubFactory(BairroFactory)

    class Meta:
        model = Quadra
        django_get_or_create = ('bairro', 'numero')


class LadoFactory(DjangoModelFactory):
    id = uuid()
    numero = factory.Sequence(lambda n: n)
    quadra = factory.SubFactory(QuadraFactory)
    logradouro = factory.SubFactory(LogradouroFactory)

    class Meta:
        model = LadoQuadra
        django_get_or_create = ('quadra', 'numero')


class ImovelFactory(DjangoModelFactory):
    id = uuid()
    lado = factory.SubFactory(LadoFactory)
    numero = factory.fuzzy.FuzzyInteger(1, 8000)
    tipo = factory.fuzzy.FuzzyChoice(Imovel.Tipo.values.keys())
    habitantes = factory.fuzzy.FuzzyInteger(0, 10)
    caes = factory.fuzzy.FuzzyInteger(0, 5)
    gatos = factory.fuzzy.FuzzyInteger(0, 5)
    ponto_estrategico = factory.fuzzy.FuzzyChoice((True, False))

    class Meta:
        model = Imovel
        django_get_or_create = ('lado', 'numero')
