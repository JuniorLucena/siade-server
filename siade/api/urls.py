# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from .views import agentes, imoveis, trabalhos

urlpatterns = patterns(
    '',
) + imoveis.urls + agentes.urls + trabalhos.urls