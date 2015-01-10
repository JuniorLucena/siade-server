from django.conf.urls import url, include, patterns
from .views import imovel, quadra, bairro, logradouro, municipio, uf

urlpatterns = patterns(
    '',
    url(r'^imovel/', include(imovel.urls, 'imovel')),
    url(r'^quadra/', include(quadra.urls, 'quadra')),
    url(r'^bairro/', include(bairro.urls, 'bairro')),
    url(r'^logradouro/', include(logradouro.urls, 'logradouro')),
    url(r'^municipio/', include(municipio.urls, 'municipio')),
    url(r'^uf/', include(uf.urls, 'uf'))
)
