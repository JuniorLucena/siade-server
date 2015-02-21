# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from .views import agentes, imoveis, trabalhos

urlpatterns = patterns(
    '',
    url(r'', include(imoveis.urls + agentes.urls + trabalhos.urls)),
)