# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item

dynamic_sitetrees = (
    tree('agentes', items=[
        item('Agentes', 'agentes:agente:listar', alias='agente', children=[
            item('{{ agente.nome }}', 'agentes:agente:detalhes agente.id', children=[
                    item('Alterar Agente', 'agentes:agente:editar agente.id',
                         access_by_perms='agentes.change_agente'),
                    item('Excluir Agente', 'agentes:agente:excluir agente.id',
                         access_by_perms='agentes.delete_agente'),
                    item('Redefinir Senha', 'agentes:agente:definir_senha agente.id',
                         access_by_perms='agentes.change_agente'),
            ], in_menu=False, in_sitetree=False),
            item('Adicionar agente', 'agentes:agente:adicionar',
                 access_by_perms='agentes.add_agente',
                 in_menu=False, in_sitetree=False),
        ]),
    ]),
)
