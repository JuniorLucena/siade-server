from random import randint, randrange
import factory
from factory.django import DjangoModelFactory
from siade.imoveis.tests.factories import MunicipioFactory
from ..models import Agente


def gerar_cpf():

    def digito_cpf(cpf):
        res = []
        for i, a in enumerate(cpf):
            b = len(cpf) + 1 - i
            res.append(b * a)
        res = sum(res) % 11

        if res > 1:
            return 11 - res
        else:
            return 0

    cpf = [randrange(10) for x in range(9)]
    cpf += [digito_cpf(cpf)]
    cpf += [digito_cpf(cpf)]

    cpfVal = 0
    for i, v in enumerate(cpf):
        cpfVal += v*(10**(len(cpf) - 1 - i))
    return cpfVal


class AgenteFactory(DjangoModelFactory):
    cpf = factory.fuzzy.FuzzyAttribute(fuzzer=gerar_cpf)
    nome = factory.Sequence(lambda n: 'Agente %d' % n)
    sobrenome = factory.Sequence(lambda n: 'Campo')
    email = factory.LazyAttribute(lambda a: '%s.%s@siade.net.br' % (
        a.nome.lower(), a.sobrenome.lower()))
    codigo = factory.LazyAttribute(lambda a: 'AG%d' % (randint(0, 99)))
    tipo = Agente.Tipo.AgenteCampo
    municipio = factory.SubFactory(MunicipioFactory)
    password = factory.PostGenerationMethodCall('set_password', 'dummy')
    ativo = True

    class Meta:
        model = Agente
        django_get_or_create = ('cpf',)
