from django.conf.urls import url, patterns
from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from sitetrees import dynamic_sitetrees
from .views import *

urlpatterns = patterns(
    '',
    url(r'^iniciar/$', iniciar_ciclo, name='iniciar'),
    url(r'^encerrar/$', encerrar_ciclo, name='encerrar'),
    url(r'^gerenciar/$', gerenciar_ciclo, name='gerenciar'),
    url(r'^distribuir_trabalhos/$', distribuir_trabalhos,
        name='distribuir_trabalhos'),
    url(r'^distribuir_trabalhos/(?P<pk>[^/]+)/$', trabalhos_alterar,
        name='distribuir_trabalhos'),
    url(r'^distribuir_trabalhos/quadras\.json$',
        trabalhos_quadras, name='trabalhos_quadras'),
    url(r'^imoveis_visitados/(?P<pk>[^/]+)/$',
        listar_imoveis_visitados, name='imoveis_visitados'),
    url(r'^alterar_ciclo/(?P<pk>[^/]+)/$', AlterarCiclo.as_view(), name='alterar_ciclo')
)

register_dynamic_trees(
    compose_dynamic_tree(dynamic_sitetrees, target_tree_alias='main',
                         parent_tree_item_alias='home'),
    reset_cache=True
)
