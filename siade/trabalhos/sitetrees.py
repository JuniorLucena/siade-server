# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item

sitetrees = (
    tree('trabalhos', items=[
        item('Gerenciamento de ciclo', '', children=[
            item('Situação do ciclo', 'ciclo:gerenciar'),
            item('Distribuir trabalhos', 'ciclo:distribuir_trabalhos'),
            item('Iniciar ciclo', 'ciclo:iniciar',
                 in_menu=False, in_sitetree=False),
            item('Encerrar ciclo', 'ciclo:encerrar',
                 in_menu=False, in_sitetree=False),
        ], access_by_perms='trabalhos.change_ciclo')
    ]),
)
