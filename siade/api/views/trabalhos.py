# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from rest_framework.generics import RetrieveAPIView
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
    url(r'^visitas/$', VisitaView.as_view(), name='visitas'),
)
