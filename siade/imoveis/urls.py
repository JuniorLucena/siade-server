from django.conf.urls import url, include, patterns
from siade.utils.urlutils import get_view_urls
from .views import quadra, bairro, logradouro, municipio, uf

quadra_urls = get_view_urls(quadra.actions, 'quadra')

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

municipio_urls = patterns(
    '',
    url(r'^$', municipio.Listar.as_view(),
        name='municipio-listar'),
    url(r'^adicionar/$', municipio.Adicionar.as_view(),
        name='municipio-adicionar'),
    url(r'^(?P<pk>\d+)/$', municipio.Detalhes.as_view(),
        name='municipio-detalhes'),
    url(r'^(?P<pk>\d+)/editar$', municipio.Editar.as_view(),
        name='municipio-editar'),
    url(r'^(?P<pk>\d+)/excluir$', municipio.Excluir.as_view(),
        name='municipio-excluir'),
)

uf_urls = patterns(
    '',
    url(r'^$', uf.Listar.as_view(),
        name='uf-listar'),
    url(r'^adicionar/$', uf.Adicionar.as_view(),
        name='uf-adicionar'),
    url(r'^(?P<pk>\d+)/$', uf.Detalhes.as_view(),
        name='uf-detalhes'),
    url(r'^(?P<pk>\d+)/editar$', uf.Editar.as_view(),
        name='uf-editar'),
    url(r'^(?P<pk>\d+)/excluir$', uf.Excluir.as_view(),
        name='uf-excluir'),
)

urlpatterns = [
    url(r'^quadra/', include(quadra_urls)),
    url(r'^logradouro/', include(logradouro_urls)),
    url(r'^bairro/', include(bairro_urls)),
    url(r'^municipio/', include(municipio_urls)),
    url(r'^uf/', include(uf_urls))
]
