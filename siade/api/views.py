# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet
from rest_sync.views import ModelSyncView, ModelSyncView_factory
from .serializers import ModelFieldsSerializer_factory
from .serializers import ImovelSyncSerializer
from .filters import AutoFilterSet
from siade.imoveis.models import *
from siade.trabalhos.models import *


class UfViewSet(ModelViewSet):
    '''
    Unidades Federativas
    '''
    queryset = UF.objects.all()
    serializer_class = ModelFieldsSerializer_factory(UF)
    search_fields = ('nome', 'sigla')


class MunicipioViewSet(ModelViewSet):
    '''
    Municípios de uma UF
    '''
    queryset = Municipio.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Municipio)
    search_fields = ('nome', 'codigo')
    filter_fields = ('uf',)


class BairroViewSet(ModelViewSet):
    '''
    Bairros de um município
    '''
    queryset = Bairro.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Bairro)
    search_fields = ('nome', 'codigo')
    filter_fields = ('municipio',)


class LogradouroViewSet(ModelViewSet):
    '''
    Logradouros de um município
    '''
    queryset = Logradouro.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Logradouro)
    search_fields = ('nome',)
    filter_fields = ('municipio',)


class QuadraViewSet(ModelViewSet):
    '''
    Quadras de imóveis de um bairro
    '''
    queryset = Quadra.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Quadra)
    filter_fields = ('numero', 'bairro')


class LadoQuadraViewSet(ModelViewSet):
    '''
    Lado de uma Quadra
    '''
    queryset = LadoQuadra.objects.all()
    serializer_class = ModelFieldsSerializer_factory(LadoQuadra)
    filter_fields = ('quadra', 'logradouro')


class TipoImovelViewSet(ModelViewSet):
    '''
    Tipos de imóvel
    '''
    queryset = TipoImovel.objects.all()
    serializer_class = ModelFieldsSerializer_factory(TipoImovel)


class ImovelViewSet(ModelViewSet):
    '''
    Dados de imóvel
    '''
    queryset = Imovel.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Imovel)
    filter_fields = ('tipo', 'caes', 'gatos', 'lado__quadra',
                     'lado__logradouro', 'lado__quadra__bairro')


class AtividadeViewSet(ModelViewSet):
    '''
    Tipos de atividades que podem ser realizadas
    '''
    queryset = Atividade.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Atividade)
    search_fields = ('nome', 'sigla')


class CicloViewSet(ModelViewSet):
    '''
    Ciclos de combate a endemias
    '''
    queryset = Ciclo.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Ciclo)
    search_fields = ('numero',)
    filter_fields = ('ano_base', 'data_inicio', 'data_fim')


class TrabalhoViewSet(ModelViewSet):
    '''
    Trabalho realizado por um agente em um ciclo
    '''
    queryset = Trabalho.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Trabalho)
    filter_fields = ('ciclo', 'agente', 'quadra', 'concluido')


class VisitaViewSet(ModelViewSet):
    '''
    Visita de um agente a um determinado imovel em um ciclo
    '''
    queryset = Visita.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Visita)
    filter_fields = (
        'data', 'ciclo', 'agente', 'imovel', 'atividade', 'tipo', 'pendencia')


class AgenteViewSet(ModelViewSet):
    '''
    Agentes de endemias
    '''
    queryset = Agente.objects.all()
    serializer_class = ModelFieldsSerializer_factory(Agente)


### SyncViews
class LogradouroSyncView(ModelSyncView):
    queryset = Logradouro.objects.all()


class QuadraSyncView(ModelSyncView):
    queryset = Quadra.objects.all()


class LadoQuadraSyncView(ModelSyncView):
    queryset = LadoQuadra.objects.all()


class ImovelSyncView(ModelSyncView):
    queryset = Imovel.objects.all().prefetch_related(
        Prefetch('visitas', Visita.objects.filter(ciclo=Ciclo.atual()))
    )
    serializer_class = ImovelSyncSerializer


class VisitaSyncView(ModelSyncView):
    queryset = Visita.objects.all()
