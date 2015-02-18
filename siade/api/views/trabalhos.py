# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_sync.views import ModelSyncView
from ..serializers import serializer_factory
from rest_sync.serializers import sync_serializer_factory
from siade.trabalhos.models import *


class CicloView(RetrieveAPIView):
    ''' Consultar dados do ciclo atual '''

    model = Ciclo
    serializer_class = serializer_factory(Ciclo)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return Ciclo.atual()


class TipoVisitalView(ListAPIView):
    ''' Listar tipos de visita '''

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        choices = []
        for val, label in Visita.Tipo.choices:
            choices.append({'id': val, 'nome': label})
        return Response(choices)


class PendenciaVisitalView(ListAPIView):
    ''' Listar tipos de pendencia de visita '''

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        choices = []
        for val, label in Visita.Pendencia.choices:
            choices.append({'id': val, 'nome': label})
        return Response(choices)


class VisitaView(ModelSyncView):
    ''' Consultar/atualizar dados das visitas do agente '''

    model = Visita
    serializer_class = sync_serializer_factory(Visita)

    def get_queryset(self):
        agente = self.request.user
        return Visita.objects.filter(agente=agente)


urls = patterns(
    '',
    url(r'^ciclo/$', CicloView.as_view(), name='ciclo'),
    url(r'^tipos-visita/$', TipoVisitalView.as_view(),
        name='tipos-visita'),
    url(r'^pendencias-visita/$', PendenciaVisitalView.as_view(),
        name='pendencias-visita'),
    url(r'^visitas/$', VisitaView.as_view(), name='visitas'),
)
