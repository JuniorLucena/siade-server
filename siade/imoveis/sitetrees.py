# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item

dynamic_sitetrees = (
    tree('imoveis', items=[
        item('Imóveis e Localidades', '#nolink', alias='cadastros', children=[
            item('Bairros, Quadras e Imóveis', 'imoveis:bairro:listar', children=[
                item('Bairro {{ bairro.nome }}', 'imoveis:bairro:detalhes bairro.id', children=[
                    item('Alterar Bairro', 'imoveis:bairro:editar bairro.id',
                         in_menu=False, in_sitetree=False),
                    item('Excluir Bairro', 'imoveis:bairro:excluir bairro.id',
                         in_menu=False, in_sitetree=False),
                    item('Quadra {{ quadra.numero }}', 'imoveis:quadra:detalhes quadra.id',
                         children=[
                            item('Editar Quadra', 'imoveis:quadra:editar quadra.id'),
                            item('Excluir Quadra', 'imoveis:quadra:excluir quadra.id')],
                         in_menu=False, in_sitetree=False),
                    item('Quadra {{ quadra.numero }}', 'imoveis:quadra:detalhes quadra.id lado.numero', children=[
                        item('{{ imovel }}', 'imoveis:imovel:detalhes imovel.id', children=[
                            item('Editar Imóvel', 'imoveis:imovel:editar imovel.id'),
                            item('Excluir Imóvel', 'imoveis:imovel:excluir imovel.id'),
                        ]),
                        item('Adicionar Imóvel', 'imoveis:imovel:adicionar lado.quadra.id lado.numero'),
                    ]),
                    item('Adicionar Quadra', 'imoveis:quadra:adicionar bairro.id'),
                ], in_menu=False, in_sitetree=False),
                item('Novo Bairro', 'imoveis:bairro:adicionar'),
            ], access_by_perms='imoveis.change_bairro'),

            item('Logradouro', 'imoveis:logradouro:listar', children=[
                item('Detalhes do Logradouro',
                     'imoveis:logradouro:detalhes logradouro.id',
                     in_menu=False, in_sitetree=False),
                item('Novo Logradouro', 'imoveis:logradouro:adicionar'),
                item('Alterar Logradouro',
                     'imoveis:logradouro:editar logradouro.id',
                     in_menu=False, in_sitetree=False),
                item('Excluir Bairro',
                     'imoveis:logradouro:excluir logradouro.id',
                     in_menu=False, in_sitetree=False)
            ], access_by_perms='imoveis.change_logradouro'),

            item('Município', 'imoveis:municipio:listar', children=[
                item('Detalhes do Município',
                     'imoveis:municipio:detalhes municipio.id',
                     in_menu=False, in_sitetree=False),
                item('Novo Município', 'imoveis:municipio:adicionar',
                     access_by_perms='imoveis.add_municipio'),
                item('Alterar Município',
                     'imoveis:municipio:editar municipio.id',
                     in_menu=False, in_sitetree=False),
                item('Excluir Município',
                     'imoveis:municipio:excluir municipio.id',
                     in_menu=False, in_sitetree=False)
            ], access_by_perms='imoveis.change_municipio'),
            item('UF', 'imoveis:uf:listar', children=[
                item('Detalhes do UF', 'imoveis:uf:detalhes uf.id',
                     in_menu=False, in_sitetree=False),
                item('Novo UF', 'imoveis:uf:adicionar'),
                item('Alterar UF', 'imoveis:uf:editar uf.id',
                     in_menu=False, in_sitetree=False),
                item('Excluir UF', 'imoveis:uf:excluir uf.id',
                     in_menu=False, in_sitetree=False)
            ], access_by_perms='imoveis.change_uf')
        ])
    ]),
)
