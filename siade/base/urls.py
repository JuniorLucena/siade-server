from django.conf.urls import patterns, url
from django.contrib.auth.views import (login, logout, password_change,
                                       password_change_done)
from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from sitetrees import dynamic_sitetrees
from .views import home


urlpatterns = patterns(
    '',
    url(r'^$',  home, name='home'),
    url(r'^alterar-senha/$', password_change, name='password_change'),
    url(r'^senha-alterada/$', password_change_done,
        name='password_change_done'),
    url(r'^login/$', login, name='user_login'),
    url(r'^logout/$', logout, {'next_page': '/login/'},
        name='user_logout'),
)

register_dynamic_trees(
    compose_dynamic_tree(dynamic_sitetrees, target_tree_alias='main',
                         parent_tree_item_alias='home'),
    reset_cache=True
)
