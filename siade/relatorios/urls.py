from django.conf.urls import patterns, include, url
from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from .sitetrees import dynamic_sitetrees
from .views import diario, semanal, qrcodes

urlpatterns = patterns(
    '',
    url(r'^diario/$', diario.form, name='diario'),
    url(r'^semanal/$', semanal.form, name='semanal'),

    url(r'^qrcode/img/$', qrcodes.qrcode_img, name='qrcode-img'),
    url(r'^qrcode/gerar/$', qrcodes.qrcode_form, name='gerar-qrcode'),
    url(r'^qrcode/imprimir\.(?P<fmt>\w+)$', qrcodes.qrcode_print,
        name='imprimir-qrcode'),
    url(r'^qrcode/imprimir\.pdf$', qrcodes.qrcode_print,
        name='imprimir-qrcode'),
)

register_dynamic_trees(
    compose_dynamic_tree(dynamic_sitetrees, target_tree_alias='main',
                         parent_tree_item_alias='home'),
    reset_cache=True
)
