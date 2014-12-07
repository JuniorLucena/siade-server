from django.conf.urls import url, include, patterns
from .views import *
from .views import bairro, logradouro

bairro_urls = patterns(
    '',
    url(r'^$', bairro.Listar.as_view(),
        name='bairro-listar'),
    url(r'^adicionar/$', bairro.Adicionar.as_view(),
        name='bairro-adicionar'),
    url(r'^(?P<pk>\d+)/$', bairro.Detalhes.as_view(),
        name='bairro-detalhes'),
    url(r'^(?P<pk>\d+)/editar$', bairro.Editar.as_view(),
        name='bairro-editar'),
    url(r'^(?P<pk>\d+)/excluir$', bairro.Excluir.as_view(),
        name='bairro-excluir'),
)

logradouro_urls = patterns(
    '',
    url(r'^$', logradouro.Listar.as_view(),
        name='logradouro-listar'),
    url(r'^adicionar/$', logradouro.Adicionar.as_view(),
        name='logradouro-adicionar'),
    url(r'^(?P<pk>\d+)/$', logradouro.Detalhes.as_view(),
        name='logradouro-detalhes'),
    url(r'^(?P<pk>\d+)/editar$', logradouro.Editar.as_view(),
        name='logradouro-editar'),
    url(r'^(?P<pk>\d+)/excluir$', logradouro.Excluir.as_view(),
        name='logradouro-excluir'),
)

urlpatterns = [
    url(r'^uf/$', UFListar.as_view(),
        name='uf-listar'),
    url(r'^uf/adicionar/$', UFAdicionar.as_view(),
        name='uf-adicionar'),
    url(r'^uf/(?P<pk>\d+)/$', UFEditar.as_view(),
        name='uf-editar'),
    url(r'^uf/(?P<pk>\d+)/apagar$', UFApagar.as_view(),
        name='uf-apagar'),

    url(r'^Municipio/$', MunicipioListar.as_view(),
        name='Municipio-listar'),
    url(r'^Municipio/adicionar/$', MunicipioAdicionar.as_view(),
        name='Municipio-adicionar'),
    url(r'^Municipio/(?P<pk>\d+)/$', MunicipioEditar.as_view(),
        name='Municipio-editar'),
    url(r'^Municipio/(?P<pk>\d+)/apagar$', MunicipioApagar.as_view(),
        name='Municipio-apagar'),

    url(r'^logradouro/', include(logradouro_urls)),
    url(r'^bairro/', include(bairro_urls))
]
