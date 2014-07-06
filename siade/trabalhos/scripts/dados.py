# -*- coding: utf-8 -*-
from random import randint, random, choice
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
	'''
	Gera dados de ciclos e visitas
	'''
	campanhas = ('Calazar', 'Chagas', 'Dengue', 'Febre Amarela', 'Raiva')
	atividades = (
		('Delimitação de Foco', 'DF'),
		('Levantamento de índice', 'LI'),
		('Levantamento de índice + Tratamento', 'LI+T'),
		('Pesquisa Vetorial Especial', 'PVE'),
		('Ponto extratégico', 'PE'),
		('Tratamento', 'T')
	)

	def gerar_agente(self):
		return (faker.first_name(), faker.last_name())

	def gerar_agentes(self, qtd):
		return [self.gerar_agente() for i in range(qtd)]

	def gerar_ciclo(self, numero=1, ano_base=faker.date_time().year):
		data_inicio = faker.date_time_between(date(ano_base, 1, 1), date(ano_base, 12, 31)).date()
		return {
			'data_inicio': data_inicio,
			'data_fim': data_inicio + timedelta(days=randint(10, 20)),
			'numero': numero,
			'ano_base': ano_base,
		}

	def gerar_ciclos(self, qtd, ano_base=faker.date_time().year):
		return [self.gerar_ciclo(i+1, ano_base) for i in range(qtd)]

	def gerar_visita(self, ciclo, agente, imovel):
		datahora_visita = faker.date_time_between(ciclo['data_inicio'], ciclo['data_fim'])
		return {
			'data': datahora_visita.date(),
			'hora': datahora_visita.time(),
			'ciclo': ciclo,
			'agente': agente,
			'imovel': imovel,
			'atividade': choice(self.atividades)
		}
