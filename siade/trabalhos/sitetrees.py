# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item
from siade.trabalhos.views import AlterarCiclo

dynamic_sitetrees = (
    tree('trabalhos', items=[
        item('Gerenciamento de ciclo', 'ciclo:gerenciar', children=[
            item('Distribuir trabalhos', 'ciclo:distribuir_trabalhos',
                 in_menu=False, in_sitetree=False),
            item('Iniciar ciclo', 'ciclo:iniciar',
                 in_menu=False, in_sitetree=False),
            item('Encerrar ciclo', 'ciclo:encerrar',
                 in_menu=False, in_sitetree=False),
            item('Imoveis Visitados', 'ciclo:imoveis_visitados agente.id',
                in_menu=False, in_sitetree=False),
            item('Editar Ciclo',  'ciclo:alterar_ciclo ciclo.id', in_menu=False, in_sitetree=False)
        ], access_by_perms='trabalhos.change_ciclo')
    ]),
)
