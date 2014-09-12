# -*- coding: utf-8 -*-
'''
Gerar dados ficticios de agentes
'''
from random import randint, randrange
from siade.agentes.models import Agente
from faker import Factory
faker = Factory.create('pt_BR')


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


def random_cpf():
    cpf = [randrange(10) for x in range(9)]
    cpf += [digito_cpf(cpf)]
    cpf += [digito_cpf(cpf)]

    cpfVal = 0
    for i, v in enumerate(cpf):
        cpfVal += v*(10**(len(cpf) - 1 - i))
    return cpfVal


def gerar_agentes(qtd):
    for i in range(qtd):
        nome = faker.first_name()
        sobrenome = faker.last_name()
        codigo = 'AG%03d' % (randint(0, 99)+i)
        cpf = random_cpf()
        Agente.objects.create(nome=nome, sobrenome=sobrenome, cpf=cpf,
                              email=faker.email(),
                              codigo=codigo,
                              tipo=Agente.Tipo.AgenteCampo)
        print '* Agente: %s (CPF %s COD %s)' % (nome, cpf, codigo)


def run(qtd=5):
    qtd = int(qtd)
    Agente.objects.all().delete()
    gerar_agentes(qtd)
