from django.conf.urls import url, include, patterns
from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from sitetrees import dynamic_sitetrees
from .views import imovel, quadra, lado, bairro, logradouro, municipio, uf

urlpatterns = patterns(
    '',
    url(r'^imovel/', include(imovel.urls, 'imovel')),
    url(r'^quadra/', include(quadra.urls, 'quadra')),
    url(r'^quadra/lado/', include(lado.urls, 'ladoquadra')),
    url(r'^bairro/', include(bairro.urls, 'bairro')),
    url(r'^logradouro/', include(logradouro.urls, 'logradouro')),
    url(r'^municipio/', include(municipio.urls, 'municipio')),
    url(r'^uf/', include(uf.urls, 'uf'))

)

register_dynamic_trees(
    compose_dynamic_tree(dynamic_sitetrees, target_tree_alias='main',
                         parent_tree_item_alias='home'),
    reset_cache=True
)
