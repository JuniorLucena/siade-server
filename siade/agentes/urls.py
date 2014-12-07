from django.conf.urls import url
from .views import agente

urlpatterns = [
    url(r'^agente/$', agente.listar.as_view(),
        name='agente-listar'),
    url(r'^agente/adicionar/$', agente.adicionar.as_view(),
        name='agente-adicionar'),
    url(r'^agente/(?P<pk>\d+)/$', agente.detalhes.as_view(),
        name='agente-detalhes'),
    url(r'^agente/(?P<pk>\d+)/editar$', agente.editar.as_view(),
        name='agente-editar'),
    url(r'^agente/(?P<pk>\d+)/excluir$', agente.excluir.as_view(),
        name='agente-excluir'),
]
