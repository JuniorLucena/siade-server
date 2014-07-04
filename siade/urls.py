from django.conf.urls import patterns, include, url
import xadmin

xadmin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(xadmin.site.urls)),
	url(r'^api/', include('siade.api.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^relatorios/', include('siade.relatorios.urls'))
)
