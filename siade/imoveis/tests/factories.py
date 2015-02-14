import factory
from factory.django import DjangoModelFactory
from ..models import (UF, Municipio, Bairro, Logradouro, Quadra,
                      LadoQuadra, Imovel)


class UFFactory(DjangoModelFactory):
    nome = factory.Sequence(lambda n: 'UF {0}'.format(n))
    sigla = factory.Sequence(lambda n: '{0}'.format(n))

    class Meta:
        model = UF


class MunicipioFactory(DjangoModelFactory):
    nome = factory.Sequence(lambda n: 'Municipio {0}'.format(n))
    uf = factory.SubFactory(UFFactory)
    codigo = factory.Sequence(lambda n: n)

    class Meta:
        model = Municipio


class BairroFactory(DjangoModelFactory):
    nome = factory.Sequence(lambda n: 'Bairro {0}'.format(n))
    municipio = factory.SubFactory(MunicipioFactory)
    codigo = factory.Sequence(lambda n: n)

    class Meta:
        model = Bairro


class LogradouroFactory(DjangoModelFactory):
    nome = factory.Sequence(lambda n: 'Rua Projetada {0}'.format(n))
    municipio = factory.SubFactory(MunicipioFactory)

    class Meta:
        model = Logradouro


class QuadraFactory(DjangoModelFactory):
    bairro = factory.SubFactory(BairroFactory)
    numero = factory.Sequence(lambda n: n)

    class Meta:
        model = Quadra


class LadoFactory(DjangoModelFactory):
    numero = factory.Sequence(lambda n: n)
    quadra = factory.SubFactory(QuadraFactory)
    logradouro = factory.SubFactory(LogradouroFactory)

    class Meta:
        model = LadoQuadra


class ImovelFactory(DjangoModelFactory):
    lado = factory.SubFactory(LadoFactory)
    numero = factory.fuzzy.FuzzyInteger(1, 8000)
    tipo = factory.fuzzy.FuzzyChoice(Imovel.Tipo.values.keys())
    habitantes = factory.fuzzy.FuzzyInteger()
    caes = factory.fuzzy.FuzzyInteger()
    gatos = factory.fuzzy.FuzzyInteger()
    ponto_estrategico = factory.fuzzy.FuzzyChoice((True, False))

    class Meta:
        model = Imovel
