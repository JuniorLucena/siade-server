from django.conf.urls import url, include
from .views import imovel, quadra, lado, bairro, logradouro, municipio, uf

urlpatterns = [
    url(r'^imovel/', include(imovel.urls)),
    url(r'^quadra/', include(quadra.urls)),
    url(r'^quadra/lado/', include(lado.urls)),
    url(r'^bairro/', include(bairro.urls)),
    url(r'^logradouro/', include(logradouro.urls)),
    url(r'^municipio/', include(municipio.urls)),
    url(r'^uf/', include(uf.urls))
]
