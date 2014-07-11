# -*- coding: utf-8 -*-
'''
Gerar dados ficticios de trabalhos
'''
from random import randint, choice
from itertools import cycle
from faker import Factory
from siade.imoveis.models import *
from ..models import *
from .dados import Gerador
from pprint import pprint
faker = Factory.create('pt_BR')

class Gerador_de_visitas(Gerador):
	def gerar_agente(self):
		nome, sobrenome = Gerador.gerar_agente(self)
		username = '%s.%s' % (nome.lower().replace(' ', ''), sobrenome.lower().replace(' ', ''))
		return Agente.objects.create(first_name=nome, last_name=sobrenome, username=username, is_staff=True)

	def gerar_ciclo(self, qtd, ano_base):
		ciclo = Gerador.gerar_ciclo(self, qtd, ano_base)
		return Ciclo.objects.create(**ciclo)

	def gerar_visita(self, ciclo, agente, imovel):
		datahora_visita = faker.date_time_between(ciclo.data_inicio, ciclo.data_fim)
		nome, sigla = choice(self.atividades)
		atividade, c = Atividade.objects.get_or_create(nome=nome, sigla=sigla)
		return Visita.objects.create(
			data=datahora_visita.date(),
			hora=datahora_visita.time(),
			ciclo=ciclo,
			agente=agente,
			imovel=imovel,
			atividade=atividade
		)

def run():
	ge = Gerador_de_visitas()
	ge.gerar_agentes(6)
	ge.gerar_ciclos(5, 2012)
	ge.gerar_ciclos(5, 2013)
	
	ciclos = Ciclo.objects.all()
	agentes = Agente.objects.all()
	quadras = Quadra.objects.all()
	quadras_por_agente = quadras.count() / agentes.count()

	visitas = []
	agente_iter = iter(agentes)
	ciclo_iter = iter(ciclos)

	quadras_count = 0
	ciclo = ciclo_iter.next()
	agente = agente_iter.next()
	for quadra in quadras:
		for imovel in Imovel.objects.filter(lado__quadra=quadra):
			print 'Visita ao imovel %s' % imovel
			visitas += [ge.gerar_visita(ciclo, agente, imovel)]
		if quadras_count < quadras_por_agente:
			quadras_count += 1
		else:
			agente = agente_iter.next()
			quadras_count = 0
		if quadras_count > 10:
			break