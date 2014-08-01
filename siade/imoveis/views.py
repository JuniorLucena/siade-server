from django.views.generic.edit import CreateView
from .models import Municipio 
from .models import Bairro
from .models import Quadra

class cidade_create(CreateView):
	model = Municipio

class bairro_create(CreateView):
	model = Bairro

class quadra_create(CreateView):
	model = Quadra
