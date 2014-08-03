# -*- coding: utf-8 -*-
from random import randint, random
from datetime import date, timedelta
from faker import Factory
faker = Factory.create('pt_BR')


def weighted_choice(weights):
    '''
    Escolhe aleatoreamente de acordo com os pesos
    '''
    rnd = random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i


class Gerador(object):

    '''
    Gera dados de imoveis e endereços
    '''
    imovel_tipos = (
        ('Residênca', 'RE'),
        ('Comércio', 'CO'),
        ('Terreno Baldio', 'TB'),
        ('Ponto estratégico', 'PE'),
        ('Outros', 'OU'),
    )

    def gerar_uf(self):
        return faker.estado()

    def gerar_municipio(self):
        return faker.city()

    def gerar_bairro_nome(self):
        return faker.bairro()

    def gerar_bairro(self, tamanho_x=randint(4, 8), tamanho_y=randint(4, 8)):
        return {
            'nome': self.gerar_bairro_nome(),
            'quadras': self.gerar_quadras(tamanho_x, tamanho_y)
        }

    def gerar_rua(self):
        return 'Rua %s' % faker.name()

    def gerar_lado_quadra(self, logradouro, qtd_imoveis, numero=1):
        return {
            'numero': numero,
            'logradouro': logradouro,
            'imoveis': self.gerar_imoveis(qtd_imoveis)
        }

    def gerar_quadra(self, numero, lados, pontos=None):
        return {
            'numero': numero,
            'lados': lados
        }

    def gerar_quadras(self, qtd_x, qtd_y, bairro=None):
        rua1 = rua2 = rua3 = rua4 = None
        ruas = [None] * 4
        quadras = []
        quadras_lista = []
        y1 = 0
        for x in range(qtd_x):
            h = weighted_choice((2, 4, 2, 2)) * 2 + 2
            ruas[2] = ruas[2] if x > 0 else self.gerar_rua()
            ruas[0] = self.gerar_rua()

            x1 = 0
            for y in range(qtd_y):
                w = randint(1, 8) * 2 + 4
                pontos = (x1, y1, x1 + w, y1 + h)
                i = len(quadras)
                li = len(quadras) - qtd_y
                ti = len(quadras) - 1
                # rua 0
                if y > 0:
                    ruas[0] = ruas[2]
                elif x > 0:
                    ruas[0] = quadras[li]['ruas'][0]
                else:
                    ruas[0] = self.gerar_rua()
                # rua 1
                if y > 0 and quadras[ti]['pontos'][1] == pontos[1]:
                    ruas[1] = quadras[ti]['ruas'][1]
                else:
                    ruas[1] = self.gerar_rua()
                # rua 2
                ruas[2] = self.gerar_rua()
                # rua 3
                if x > 0:
                    ruas[3] = quadras[li]['ruas'][1]
                elif y > 0:
                    ruas[3] = quadras[ti]['ruas'][3]
                else:
                    ruas[3] = self.gerar_rua()

                numero = x * qtd_y + abs((qtd_y * (x % 2) - y)) + 1 - (x % 2)
                quadras += [{'pontos': pontos, 'ruas': list(ruas)}]
                tamanhos = [w, h] * 2
                imoveis_numeros = [
                    range(x * 20 + 1, (x + 1) * 20 + 1, 2),
                    range(y * 10 + 1, (y + 1) * 10 + 1, 2),
                    range(x * 20 + 2, (x + 1) * 20 + 2, 2),
                    range(y * 10 + 2, (y + 1) * 10 + 2, 2),
                ]
                lados = [self.gerar_lado_quadra(
                    ruas[i], imoveis_numeros[i], i + 1) for i in range(4)]
                quadras_lista += [self.gerar_quadra(numero, lados, pontos)]
                x1 += w + 2
            y1 += h + 2
        return quadras_lista

    def gerar_imovel(self, ordem=0, numero=None):
        imovel = {
            'tipo': self.imovel_tipos[weighted_choice((3, 3, 1, 2, 1))],
            'habitantes': weighted_choice((0, 2, 3, 3, 2, 1)),
            'caes': weighted_choice((2, 3, 1, 1)),
            'gatos': weighted_choice((2, 3, 1, 1)),
            'ordem': ordem,
        }
        if numero:
            imovel['numero'] = numero
        if imovel['tipo'] == 'Terreno Baldio':
            imovel['habitantes'] = 0
        return imovel

    def gerar_imoveis(self, numeros):
        if hasattr(numeros, '__iter__'):
            return [self.gerar_imovel(
                i + 1, num) for i, num in enumerate(numeros)]
        else:
            return [self.gerar_imovel(i + 1) for i in range(numeros)]

    def gerar_agente(self, qtd):
        return {
            'nome': faker.first_name(),
            'sobrenome': faker.last_name()
        }

    def gerar_ciclo(self, numero=1, ano_base=faker.date_time().year):
        data_inicio = date(
            ano_base, faker.date_time().month, faker.date_time().day)
        return {
            'data_inicio': data_inicio,
            'data_fim': data_inicio + timedelta(days=randint(10, 20)),
            'numero': numero,
            'ano_base': ano_base,
        }

    def gerar_ciclos(self, qtd, ano_base=faker.date_time().year):
        return [self.gerar_ciclo(i + 1, ano_base) for i in range(qtd)]

    def gerar_trabalhos(self, ciclo, quadras):
        pass
