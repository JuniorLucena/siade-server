from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import xadmin

xadmin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base_site.html')),
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^api/', include('siade.api.urls')),
    url(r'^api/sync/', include('rest_sync.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls')),
    url(r'^relatorios/', include('siade.relatorios.urls'))
)
