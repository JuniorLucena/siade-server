import xadmin
from .models import *

class AgenteAdmin(object):
	list_display = ('first_name', 'last_name', 'username')
	relfield_style = 'fk-ajax'

class AtividadeAdmin(object):
	list_display = ('nome', 'sigla')
	search_fields = ('nome',)

class CicloAdmin(object):
	list_display = ('numero', 'ano_base', 'data_inicio', 'data_fim')
	list_filter = ('numero', 'ano_base', 'data_inicio', 'data_fim')
	relfield_style = 'fk-ajax'

class TrabalhoAdmin(object):
	list_display = ('ciclo', 'agente', 'quadra', 'concluido')
	list_filter = ('ciclo', 'agente', 'quadra', 'concluido')

class VisitaAdmin(object):
	list_display = ('data', 'hora', 'imovel', 'ciclo', 'agente', 'tipo', 'atividade', 'pendencia')
	list_filter = ('data', 'imovel', 'ciclo', 'agente', 'tipo', 'atividade', 'pendencia')

xadmin.site.register(Agente, AgenteAdmin)
xadmin.site.register(Atividade, AtividadeAdmin)
xadmin.site.register(Ciclo, CicloAdmin)
xadmin.site.register(Trabalho, TrabalhoAdmin)
xadmin.site.register(Visita, VisitaAdmin)