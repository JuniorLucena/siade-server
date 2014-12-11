from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.views import password_change, password_change_done
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html'),
        name='home'),
    url(r'^usuario/alterar-senha/$', password_change,
        {'template_name': 'alterar_senha_form.html'},
        name="password_change"),
    url(r'^usuario/senha-alterada/$', password_change_done,
        {'template_name': 'alterar_senha_done.html'},
        name="password_change_done"),
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
