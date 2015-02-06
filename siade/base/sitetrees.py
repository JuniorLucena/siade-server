# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item

sitetrees = (
    tree('main', title='Menu principal', items=[
         item('Início', 'home', alias='home', in_menu=True, in_sitetree=True),
    ]),
)