from django.conf.urls import patterns, url
from django.contrib.auth.views import (login, logout, password_change,
                                       password_change_done)
from .views import home, password_reset

urlpatterns = patterns(
    '',
    url(r'^$',  home, name='home'),
    url(r'^usuario/redefinir-senha/(?P<user>\d+)/$', password_reset,
        name='password_reset'),
    url(r'^usuario/alterar-senha/$', password_change,
        name='password_change'),
    url(r'^usuario/senha-alterada/$', password_change_done,
        name='password_change_done'),
    url(r'^usuario/login/$', login, name='user_login'),
    url(r'^usuario/logout/$', logout, {'next_page': '/usuario/login/'},
        name='user_logout'),
)
