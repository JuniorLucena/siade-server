from django.conf.urls import patterns, include, url
from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from .sitetrees import dynamic_sitetrees
import views
from .views import qrcodes, diario_d1

urlpatterns = patterns(
    '',
    url(r'^bairro/$', views.estatisticas_bairro),
    url(r'^quadra\.(\w+)$', views.rel_quadra, name='relatorio_quadra'),
    url(r'^pendencia\.(\w+)$', views.casas_pendentes, name='casas_pendentes'),
    url(r'^diario/([0-9]{4})-([0-9]{2})-([0-9]+)\.(\w+)$', views.rel_diario, name='relatorio_D1'),
    url(r'^relatorio/d1_form/$', diario_d1.d1_form, name='form_d1'),
    url(r'^semanal/([0-9]+)\.(\w+)$$', views.rel_semanal, name='relatorio_D7'),
    url(r'^agente/$', views.estatisticas_agente),

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
