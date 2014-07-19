# -*- coding: utf-8 -*-
from django.db.models import Avg, Count, Sum
from rest_framework import viewsets, mixins, generics
from rest_framework.views import APIView
from rest_framework.decorators import link, action
from rest_framework.response import Response
from .serializers import *
from .filters import AutoFilterSet
from siade.imoveis.models import *
from siade.trabalhos.models import *

class UfViewSet(viewsets.ModelViewSet):
	'''
	Unidades Federativas
	'''
	model = UF
	search_fields = ('nome', 'sigla')

class MunicipioViewSet(viewsets.ModelViewSet):
	'''
	Municípios de uma UF
	'''
	model = Municipio
	search_fields = ('nome', 'codigo')
	filter_fields = ('uf',)

class BairroViewSet(viewsets.ModelViewSet):
	'''
	Bairros de um município
	'''
	model = Bairro
	search_fields = ('nome', 'codigo')
	filter_fields = ('municipio',)

class LogradouroViewSet(viewsets.ModelViewSet):
	'''
	Logradouros de um município
	'''
	model = Logradouro
	search_fields = ('nome',)
	filter_fields = ('municipio',)

class QuadraViewSet(viewsets.ModelViewSet):
	'''
	Quadras de imóveis de um bairro
	'''
	model = Quadra
	serializer_class = QuadraSerializer
	filter_fields = ('numero', 'bairro')

class LadoQuadraViewSet(viewsets.ModelViewSet):
	'''
	Lado de uma Quadra
	'''
	model = LadoQuadra
	serializer_class = LadoSerializer
	filter_fields = ('quadra', 'logradouro')

class TipoImovelViewSet(viewsets.ModelViewSet):
	'''
	Tipos de imóvel
	'''
	model = TipoImovel

class ImovelViewSet(viewsets.ModelViewSet):
	'''
	Dados de imóvel
	'''
	model = Imovel
	serializer_class = ImovelSerializer
	filter_fields = ('tipo', 'caes', 'gatos', 'lado__quadra', 'lado__logradouro', 'lado__quadra__bairro')

class AgenteViewSet(viewsets.ModelViewSet):
	'''
	Agentes de endemias
	'''
	model = Agente
	serializer_class = AgenteSerializer
	search_fields = ('first_name', 'last_name')
	filter_fields = ('is_active', 'is_staff')

####
class AtividadeViewSet(viewsets.ModelViewSet):
	'''
	Tipos de atividades que podem ser realizadas
	'''
	model = Atividade
	search_fields = ('nome', 'sigla')

class CicloViewSet(viewsets.ModelViewSet):
	'''
	Ciclos de combate a endemias
	'''
	model = Ciclo
	search_fields = ('numero',)
	filter_fields = ('ano_base', 'data_inicio', 'data_fim')

class TrabalhoViewSet(viewsets.ModelViewSet):
	'''
	Trabalho realizado por um agente em um ciclo
	'''
	model = Trabalho
	filter_fields = ('ciclo', 'agente', 'quadra', 'concluido')

class VisitaViewSet(viewsets.ModelViewSet):
	'''
	Visita de um agente a um determinado imovel em um ciclo
	'''
	model = Visita
	serializer_class = VisitaSerializer
	filter_fields = ('data', 'ciclo', 'agente', 'imovel', 'atividade', 'tipo', 'pendencia')
