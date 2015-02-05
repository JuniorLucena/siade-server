from django.conf.urls import url, include
from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from sitetrees import dynamic_sitetrees
from .views import agente

urlpatterns = [
    url(r'^agente/', include(agente.urls, 'agente'))
]

register_dynamic_trees(
    compose_dynamic_tree(dynamic_sitetrees, target_tree_alias='main',
                         parent_tree_item_alias='home'),
    reset_cache=True
)