from django.conf.urls import patterns, include, url
from .views import cidade_create
from .views import bairro_create
from .views import quadra_create

urlpatterns = patterns('',
	url(r'^cidade/add', cidade_create.as_view()),
	url(r'^bairro/add', bairro_create.as_view()),
	url(r'^quadra/add', quadra_create.as_view()),
)
