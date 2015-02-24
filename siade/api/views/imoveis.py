# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_sync.views import ModelSyncView
from rest_sync.serializers import sync_serializer_factory
from siade.imoveis.models import *
from siade.trabalhos.models import Ciclo


class BairroView(ModelSyncView):
    ''' Listar bairros de município '''

    model = Bairro
    serializer_class = sync_serializer_factory(Bairro)
    fields = ('nome',)

    def get_queryset(self):
        agente = self.request.user
        trabalhos = agente.trabalhos.filter(ciclo=Ciclo.atual())\
                          .values_list('quadra__bairro', flat=True)
        return Bairro.objects.filter(id__in=set(trabalhos))


class LogradouroView(ModelSyncView):
    ''' Consultar/atualizar Logradouros do município '''

    model = Logradouro
    serializer_class = sync_serializer_factory(Logradouro)

    def get_queryset(self):
        agente = self.request.user
        return Logradouro.objects.filter(municipio=agente.municipio)


class QuadraView(ModelSyncView):
    ''' Consultar/atualizar quadras de um bairro '''

    model = Quadra
    serializer_class = sync_serializer_factory(Quadra)

    def get_queryset(self):
        agente = self.request.user
        return Quadra.objects.filter(trabalhos__agente=agente)


class LadoQuadraView(ModelSyncView):
    ''' Consultar/atualizar lados das quadras '''

    model = LadoQuadra
    serializer_class = sync_serializer_factory(LadoQuadra)

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

    model = Imovel
    serializer_class = sync_serializer_factory(Imovel)

    def get_queryset(self):
        agente = self.request.user
        return Imovel.objects.filter(lado__quadra__trabalhos__agente=agente)


urls = patterns(
    '',
    url(r'^bairros/$', BairroView.as_view(), name='bairros'),
    url(r'^logradouros/$', LogradouroView.as_view(), name='logradouros'),
    url(r'^quadras/$', QuadraView.as_view(), name='quadras'),
    url(r'^lados/$', LadoQuadraView.as_view(), name='lados'),
    url(r'^tipos-imovel/$', TipoImovelView.as_view(), name='tipos-imovel'),
    url(r'^imoveis/$', ImovelView.as_view(), name='imoveis'),
)
