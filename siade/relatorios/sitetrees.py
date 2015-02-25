# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item

dynamic_sitetrees = (
    tree('relatorios', items=[
        item('Gerar QR-Code', 'relatorios:gerar-qrcode'),
    ]),
)
