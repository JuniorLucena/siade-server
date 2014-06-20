from django.conf.urls import patterns, include, url
import xadmin
import api

xadmin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^api/', include(api.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
