from django.conf.urls import url, include, patterns
from .views import agente

agente_urls = patterns(
    '',
    url(r'^$', agente.Listar.as_view(),
        name='agente-listar'),
    url(r'^adicionar/$', agente.Adicionar.as_view(),
        name='agente-adicionar'),
    url(r'^(?P<pk>\d+)/$', agente.Detalhes.as_view(),
        name='agente-detalhes'),
    url(r'^(?P<pk>\d+)/editar$', agente.Editar.as_view(),
        name='agente-editar'),
    url(r'^(?P<pk>\d+)/excluir$', agente.Excluir.as_view(),
        name='agente-excluir'),
)

urlpatterns = [
    url(r'^agente/', include(agente_urls))
]
