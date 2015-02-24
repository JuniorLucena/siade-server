# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item

sitetrees = (
    tree('main', title='Menu principal', items=[
        item('Início', 'home', alias='home',
             in_menu=True, in_sitetree=True),
    ]),
)

dynamic_sitetrees = (
    tree('dynamic_main', items=[
        item('Alterar senha', 'password_change',
             in_menu=False, in_sitetree=False),
        item('Gerar QrCode ', 'imprimir-qrcode'),
    ]),
)
