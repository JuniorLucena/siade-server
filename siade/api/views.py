# -*- coding: utf-8 -*-
from django.db.models import Avg, Count, Sum
from rest_framework import viewsets, mixins, generics
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
	search_fields = ('nome', 'sobrenome')
	filter_fields = ('ativo',)

####
class CampanhaViewSet(viewsets.ModelViewSet):
	'''
	Campanhas de combate a endemias
	'''
	model = Campanha
	search_fields = ('nome',)

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

	@link()
	def trabalhos(self, request, pk=None):
		qs = Trabalho.objects.filter(ciclo=pk)
		filter_class = AutoFilterSet(qs)
		trabalhos = filter_class(request.QUERY_PARAMS, queryset=qs).qs
		quadras = Quadra.objects.filter(trabalhos=trabalhos)
		imoveis = Imovel.objects.filter(lado__quadra=quadras)
		visitas = Visita.objects.filter(imovel__lado__quadra=quadras)
		por_tipo = imoveis.values('tipo', 'tipo__nome').annotate(total=Count('id')).order_by()
		data = {
			'imoveis': {
				'total': imoveis.count(),
				'por_tipo': por_tipo,
				'trabalhados': {
					'total': imoveis.filter(visitas=visitas).count(),
					'por_tipo': por_tipo.filter(visitas=visitas),
				}
			}
		}
		return Response(data)

class TrabalhoViewSet(viewsets.ModelViewSet):
	'''
	Trabalho realizado por um agente em um ciclo
	'''
	model = Trabalho
	filter_fields = ('ciclo', 'agente', 'campanha', 'quadra', 'concluido')

	@link()
	def distribuir(self, request, pk=None):
		quadras = Quadra.objects.all().order_by('bairro').values('id').annotate(imoveis=Count('lados__imoveis'))
		return Response(quadras)

class VisitaViewSet(viewsets.ModelViewSet):
	'''
	Visita de um agente a um determinado imovel em um ciclo
	'''
	model = Visita
	serializer_class = VisitaSerializer
	filter_fields = ('data', 'ciclo', 'agente', 'imovel', 'tipo', 'pendencia')
