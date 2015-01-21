from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url(r'^bairro/$', views.estatisticas_bairro),
    url(r'^quadra\.(\w+)$', views.rel_quadra),
    url(r'^pendencia\.(\w+)$', views.casas_pendentes),
    url(r'^diario/([0-9]{4})-([0-9]{2})-([0-9]+)\.(\w+)$', views.rel_diario),
    url(r'^semanal/([0-9]+)\.(\w+)$$', views.rel_semanal),
)
