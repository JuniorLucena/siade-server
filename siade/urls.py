from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', login_required(
        TemplateView.as_view(template_name='base_site.html')
    )),
    url(r'^agentes/', include('siade.agentes.urls')),
    url(r'^imoveis/', include('siade.imoveis.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('siade.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls')),
    url(r'^relatorios/', include('siade.relatorios.urls')),
    url(r'^qrcode/', 'siade.views.qrcode'),
)
