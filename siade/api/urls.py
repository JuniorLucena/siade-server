# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from .views import *

register = {
    'imoveis/uf': UfViewSet,
    'imoveis/municipio': MunicipioViewSet,
    'imoveis/bairro': BairroViewSet,
    'imoveis/quadra': QuadraViewSet,
    'imoveis/lado-quadra': LadoQuadraViewSet,
    'imoveis/logradouro': LogradouroViewSet,
    'imoveis/tipo-imovel': TipoImovelViewSet,
    'imoveis/imovel': ImovelViewSet,
    'trabalhos/agente': AgenteViewSet,
    'trabalhos/atividade': AtividadeViewSet,
    'trabalhos/trabalho': TrabalhoViewSet,
    'trabalhos/ciclo': CicloViewSet,
    'trabalhos/visita': VisitaViewSet,
}

router = DefaultRouter()
for (prefix, view) in register.items():
    router.register(prefix, view)

urlpatterns = router.urls
