# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sitetree.utils import tree, item

dynamic_sitetrees = (
	tree('relatorios', items=[
		item('Relatórios', '#nolink', alias='relatorios', children=[
			 #item('D1 - Diário', 'relatorios:relatorio_D1 pdf'),
			 item('D1 - Diário', 'relatorios:form_d1'),
			 item('D7 - Semanal', 'relatorios:form_d7'),
			 item('Ciclo', 'relatorios:form_ciclo'),
			 #item('D7 - Semanal', 'relatorios:relatorio_D7 pdf'),			 
			 #item('Ciclo', 'relatorios:relatorio_Ciclo pdf'),			 
			 item('Casas Pendentes', 'relatorios:casas_pendentes pdf'),
		])
	]),

    tree('relatorios', items=[
        item('Gerar QR-Code', 'relatorios:gerar-qrcode'),
    ]),
)

