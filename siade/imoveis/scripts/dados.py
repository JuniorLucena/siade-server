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

def weighted_choice_dict(weights_dict):
	'''
	Escolhe aleatoreamente de acordo com os pesos usando um dicionario
	'''
	weights = weights_dict.values()
	rnd = random() * sum(weights)
	for i, w in enumerate(weights):
		rnd -= w
		if rnd < 0:
			return weights_dict.keys()[i]

class Gerador(object):
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
		ruas = [None]*4
		quadras = []
		quadras_lista = []
		y1 = 0
		for x in range(qtd_x):
			h = weighted_choice((2, 4, 2, 2)) * 2 + 2
			ruas[2] = ruas[2] if x > 0 else self.gerar_rua()
			ruas[0] = self.gerar_rua()
			
			x1 = 0
			for y in range(qtd_y):
				w = randint(1,8) * 2 + 4
				pontos = (x1, y1, x1+w, y1+h)
				li = (x-1) * qtd_y + y

				x2 = x1+w
				y2 = y1+h

				if x > 0 and quadras[li]['pontos'][1] == y1:
					ruas[1] = quadras[li]['ruas'][1]
				elif y > 0:
					ruas[1] = ruas[3]
				else:
					ruas[1] = self.gerar_rua()

				if x > 0 and quadras[li]['pontos'][3] == y2:
					ruas[3] = quadras[li]['ruas'][3]
				else:
					ruas[3] = self.gerar_rua()

				numero = x * qtd_y + abs((qtd_y * (x % 2) - y)) + 1 - (x % 2)
				quadras += [{'pontos': pontos, 'ruas': list(ruas)}]
				tamanhos = [w, h]*2
				lados = [self.gerar_lado_quadra(ruas[i], tamanhos[i], i+1) for i in range(4)]
				quadras_lista += [self.gerar_quadra(numero, lados, pontos)]
				x1 += w+2
			y1 += h+2
		return quadras_lista

	def gerar_imovel(self, ordem=0):
		tipos = {'Residênca': 3, 'Comércio': 2, 'Terreno Baldio': 1, 'Ponto estratégico': 1, 'Outros': 1}
		habitantes = {1: 2, 2: 3, 3: 3, 4: 2, 5: 1}
		caes = {0: 2, 1: 3, 2: 1, 3: 1}
		gatos = {0: 2, 1: 3, 2: 1, 3: 1}
		imovel = {
			'tipo': weighted_choice_dict(tipos),
			'habitantes': weighted_choice_dict(habitantes),
			'caes': weighted_choice_dict(caes),
			'gatos': weighted_choice_dict(gatos),
			'ordem': ordem,
		}
		if imovel['tipo'] == 'Terreno Baldio':
			imovel['habitantes'] = 0
		return imovel

	def gerar_imoveis(self, qtd):
		return [self.gerar_imovel(i+1) for i in range(qtd)]

	def gerar_agente(self, qtd):
		return {
			'nome': faker.first_name(),
			'sobrenome': faker.last_name()
		}

	def gerar_ciclo(self, numero=1, ano_base=faker.date_time().year):
		data_inicio = date(ano_base, faker.date_time().month, faker.date_time().day)
		return {
			'data_inicio': data_inicio,
			'data_fim': data_inicio + timedelta(days=randint(10, 20)),
			'numero': numero,
			'ano_base': ano_base,
		}

	def gerar_ciclos(self, qtd, ano_base=faker.date_time().year):
		return [self.gerar_ciclo(i+1, ano_base) for i in range(qtd)]

	def gerar_trabalhos(self, ciclo, quadras):
		pass
