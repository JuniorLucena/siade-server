from django.contrib import admin
from .models import Agente


class AgenteAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'sobrenome')
    list_filter = []
    relfield_style = 'fk-ajax'

admin.site.register(Agente, AgenteAdmin)
