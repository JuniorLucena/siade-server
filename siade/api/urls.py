# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from .views import *

register = {
    'agente': AgenteViewSet,
    'imoveis/uf': UfViewSet,
    'imoveis/municipio': MunicipioViewSet,
    'imoveis/bairro': BairroViewSet,
    'imoveis/quadra': QuadraViewSet,
    'imoveis/lado-quadra': LadoQuadraViewSet,
    'imoveis/logradouro': LogradouroViewSet,
    'imoveis/tipo-imovel': TipoImovelViewSet,
    'imoveis/imovel': ImovelViewSet,
    'trabalhos/atividade': AtividadeViewSet,
    'trabalhos/trabalho': TrabalhoViewSet,
    'trabalhos/ciclo': CicloViewSet,
    'trabalhos/visita': VisitaViewSet,
}

router = DefaultRouter()
for (prefix, view) in register.items():
    router.register(prefix, view)

urlpatterns = patterns(
    '',  # sync views
    url(r'^sync/imoveis/logradouro/', LogradouroSyncView.as_view()),
    url(r'^sync/imoveis/quadra/', QuadraSyncView.as_view()),
    url(r'^sync/imoveis/ladoquadra/', LadoQuadraSyncView.as_view()),
    url(r'^sync/imoveis/imovel/', ImovelSyncView.as_view()),
    url(r'^sync/trabalhos/visita/', VisitaSyncView.as_view())
) + router.urls
