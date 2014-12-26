from django.conf.urls import url, include
from .views import imovel, quadra, lado, bairro, logradouro, municipio, uf

urlpatterns = [
    url(r'^imovel/', include(imovel.urls, 'imovel')),
    url(r'^quadra/', include(quadra.urls, 'quadra')),
    url(r'^quadra/lado/', include(lado.urls, 'ladoquadra')),
    url(r'^bairro/', include(bairro.urls, 'bairro')),
    url(r'^logradouro/', include(logradouro.urls, 'logradouro')),
    url(r'^municipio/', include(municipio.urls, 'municipio')),
    url(r'^uf/', include(uf.urls, 'uf'))
]
