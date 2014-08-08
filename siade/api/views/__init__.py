# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework_bulk import mixins as bulk_mixins
from ..serializers import *
from ..filters import AutoFilterSet
from siade.imoveis.models import *
from siade.trabalhos.models import *


class UsuarioViewSet(ModelViewSet):
    '''
    Usuário do sistema
    '''
    model = get_user_model()
    serializer_class = UsuarioSerializer


class UfViewSet(ModelViewSet):
    '''
    Unidades Federativas
    '''
    model = UF
    search_fields = ('nome', 'sigla')


class MunicipioViewSet(ModelViewSet):
    '''
    Municípios de uma UF
    '''
    model = Municipio
    search_fields = ('nome', 'codigo')
    filter_fields = ('uf',)


class BairroViewSet(ModelViewSet):
    '''
    Bairros de um município
    '''
    model = Bairro
    search_fields = ('nome', 'codigo')
    filter_fields = ('municipio',)


class LogradouroViewSet(ModelViewSet):
    '''
    Logradouros de um município
    '''
    model = Logradouro
    search_fields = ('nome',)
    filter_fields = ('municipio',)


class QuadraViewSet(ModelViewSet):
    '''
    Quadras de imóveis de um bairro
    '''
    model = Quadra
    serializer_class = QuadraSerializer
    filter_fields = ('numero', 'bairro')


class LadoQuadraViewSet(ModelViewSet):
    '''
    Lado de uma Quadra
    '''
    model = LadoQuadra
    serializer_class = LadoSerializer
    filter_fields = ('quadra', 'logradouro')


class TipoImovelViewSet(ModelViewSet):
    '''
    Tipos de imóvel
    '''
    model = TipoImovel


class ImovelViewSet(ModelViewSet):
    '''
    Dados de imóvel
    '''
    model = Imovel
    serializer_class = ImovelSerializer
    filter_fields = ('tipo', 'caes', 'gatos', 'lado__quadra',
                     'lado__logradouro', 'lado__quadra__bairro')


class AgenteViewSet(ModelViewSet):
    '''
    Agentes de endemias
    '''
    model = Agente
    serializer_class = AgenteSerializer
    search_fields = ('first_name', 'last_name')
    filter_fields = ('is_active', 'is_staff')


class AtividadeViewSet(ModelViewSet):
    '''
    Tipos de atividades que podem ser realizadas
    '''
    model = Atividade
    search_fields = ('nome', 'sigla')


class CicloViewSet(ModelViewSet):
    '''
    Ciclos de combate a endemias
    '''
    model = Ciclo
    search_fields = ('numero',)
    filter_fields = ('ano_base', 'data_inicio', 'data_fim')


class TrabalhoViewSet(ModelViewSet):
    '''
    Trabalho realizado por um agente em um ciclo
    '''
    model = Trabalho
    filter_fields = ('ciclo', 'agente', 'quadra', 'concluido')


class VisitaViewSet(ModelViewSet):
    '''
    Visita de um agente a um determinado imovel em um ciclo
    '''
    model = Visita
    serializer_class = VisitaSerializer
    filter_fields = (
        'data', 'ciclo', 'agente', 'imovel', 'atividade', 'tipo', 'pendencia')
