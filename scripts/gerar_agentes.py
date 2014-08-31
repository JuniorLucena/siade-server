from random import randint
from siade.agentes.models import Agente
from faker import Factory
faker = Factory.create('pt_BR')


def gerar_agentes(qtd):
    for i in range(qtd):
        nome, sobrenome = faker.first_name(), faker.last_name()
        codigo = 'AG%03d' % (randint(0, 99)+i)
        Agente.objects.create(nome=nome, sobrenome=sobrenome,
                              codigo=codigo, nivel=1)
        print '%s %s (%s)' % (nome, sobrenome, codigo)


def run(qtd=5):
    qtd = int(qtd)
    Agente.objects.all().delete()
    gerar_agentes(qtd)
