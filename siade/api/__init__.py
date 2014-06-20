# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from .views import *

register = {
	'imoveis/uf': UfViewSet,
	'imoveis/municipio': MunicipioViewSet,
	'imoveis/bairro': BairroViewSet,
	'imoveis/quadra': QuadraViewSet,
	'imoveis/logradouro': LogradouroViewSet,
	'imoveis/tipo-imovel': TipoImovelViewSet,
	'imoveis/imovel': ImovelViewSet,
	'trabalhos/agente': AgenteViewSet,
	'trabalhos/campanha': CampanhaViewSet,
	'trabalhos/atividade': AtividadeViewSet,
	'trabalhos/trabalho': TrabalhoViewSet,
	'trabalhos/ciclo': CicloViewSet,
	'trabalhos/visita': VisitaViewSet,
}

router = DefaultRouter()
for (prefix, view) in register.items():
	router.register(prefix, view)

urls = router.urls