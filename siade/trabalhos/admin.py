from django.contrib import admin
from .models import *


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome',)


class CicloAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ano_base', 'data_inicio', 'data_fim')
    list_filter = ('numero', 'ano_base', 'data_inicio', 'data_fim')
    relfield_style = 'fk-ajax'


class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ('ciclo', 'agente', 'concluido')
    list_filter = ('ciclo', 'agente', 'concluido')


class VisitaAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'imovel', 'ciclo', 'agente',
                    'tipo', 'atividade', 'pendencia')
    list_filter = ('data', 'ciclo', 'agente', 'tipo',
                   'atividade', 'pendencia')

admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(Ciclo, CicloAdmin)
admin.site.register(Trabalho, TrabalhoAdmin)
admin.site.register(Visita, VisitaAdmin)
