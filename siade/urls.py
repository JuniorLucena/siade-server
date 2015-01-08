from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^agentes/', include('siade.agentes.urls', 'agentes')),
    url(r'^imoveis/', include('siade.imoveis.urls', 'imoveis')),
    url(r'^trabalhos/', include('siade.trabalhos.urls', 'trabalhos')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('siade.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls')),
    url(r'^relatorios/', include('siade.relatorios.urls')),
    url(r'', include('siade.base.urls')),
)
