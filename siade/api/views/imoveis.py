# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_sync.views import ModelSyncView
from ..serializers import serializer_factory
from siade.imoveis.models import *


class BairroView(ListAPIView):
    ''' Listar bairros de município em que o agente trabalha '''

    model = Bairro
    serializer_class = serializer_factory(Bairro)
    fields = ('nome',)
    
    def get_queryset(self):
        agente = self.request.user
        return Bairro.objects.filter(municipio=agente.municipio)


class LogradouroView(ModelSyncView):
    ''' Consultar/atualizar Logradouros do município em que o agente trabalha '''
    
    model = Logradouro
    serializer_class = serializer_factory(Logradouro)

    def get_queryset(self):
        agente = self.request.user
        return Logradouro.objects.filter(municipio=agente.municipio)


class QuadraView(ModelSyncView):
    ''' Consultar/atualizar quadras de imóveis de um bairro em que o agente trabalha'''

    model = Quadra
    serializer_class = serializer_factory(Quadra)

    def get_queryset(self):
        agente = self.request.user
        return Quadra.objects.filter(trabalhos__agente=agente)


class LadoQuadraView(ModelSyncView):
    ''' Consultar/atualizar Lado de uma Quadra '''

    model = LadoQuadra
    serializer_class = serializer_factory(LadoQuadra)

    def get_queryset(self):
        agente = self.request.user
        return LadoQuadra.objects.filter(quadra__trabalhos__agente=agente)

class TipoImovelView(ListAPIView):
    ''' Listar tipos de imóvel '''

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        choices = []
        for val, label in Imovel.Tipo.choices:
            choices.append({'id': val, 'nome': label})
        return Response(choices)


class ImovelView(ModelSyncView):
    ''' Consultar ou atualizar dados de imóvel '''
    queryset = Imovel.objects.all()
    serializer_class = serializer_factory(Imovel)

    def get_queryset(self):
        agente = self.request.user
        return Imovel.objects.filter(lado__quadra__trabalhos__agente=agente)

urls = patterns(
    '',
    url(r'^bairros/$', BairroView.as_view()),
    url(r'^logradouros/$', LogradouroView.as_view()),
    url(r'^quadras/$', QuadraView.as_view()),
    url(r'^lados/$', LadoQuadraView.as_view()),
    url(r'^tipos-imovel/$', TipoImovelView.as_view()),
    url(r'^imoveis/$', ImovelView.as_view()),
)
