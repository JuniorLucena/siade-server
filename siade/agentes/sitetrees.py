# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item

dynamic_sitetrees = (
    tree('agentes', items=[
        item('Agentes', '#', children=[
            item('Cadastro de Agente', 'agentes:agente:listar', children=[
                item('{{ agente.nome }}', 'agentes:agente:detalhes agente.id', children=[
                        item('Alterar Agente', 'agentes:agente:editar agente.id',
                             in_menu=False, in_sitetree=False,
                             access_by_perms='agentes.change_agente'),
                        item('Excluir Agente', 'agentes:agente:excluir agente.id',
                             in_menu=False, in_sitetree=False,
                             access_by_perms='agentes.delete_agente'),
                ]),
                item('Adicionar agente', 'agentes:agente:adicionar',
                     access_by_perms='agentes.add_agente'),
            ]),
        ]),
    ]),
)
