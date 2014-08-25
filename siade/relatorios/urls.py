from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^diario/([0-9]{4})-([0-9]{2})-([0-9]+)/$', views.rel_diario),
    url(r'^semanal/([0-9]+)/$', views.rel_semanal),
)
