from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.views import password_change, password_change_done
from django.contrib.auth.forms import AdminPasswordChangeForm

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='home.html'),
        name='home'),
    url(r'^usuario/redefinir-senha/$', password_change,
        {'password_change_form': AdminPasswordChangeForm},
        name='password_reset'),
    url(r'^usuario/alterar-senha/$', password_change,
        name='password_change'),
    url(r'^usuario/senha-alterada/$', password_change_done,
        name='password_change_done'),
    url(r'^usuario/login/$', 'django.contrib.auth.views.login',
        name='user_login'),
    url(r'^usuario/logout/$', 'django.contrib.auth.views.logout',
        name='user_logout'),
)
