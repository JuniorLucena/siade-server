from django.contrib import admin
from .models import *


class UfAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome',)


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome',)
    list_filter = ('uf',)


class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'municipio')
    search_fields = ('nome',)
    list_filter = ('municipio',)
    relfield_style = 'fk-ajax'


class LadoQuadraInline(admin.TabularInline):
    model = LadoQuadra
    style = 'table'
    list_display = ('logradouro')
    verbose_name_plural = 'lados'


class QuadraAdmin(admin.ModelAdmin):
    list_display = ('numero', 'bairro')
    list_filter = ('bairro',)
    ordering = ('bairro__nome', 'numero')
    batch_fields = ('bairro',)
    inlines = (LadoQuadraInline,)


class LogradouroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'municipio')
    search_fields = ('nome',)
    list_filter = ('municipio',)
    relfield_style = 'fk-ajax'


class TipoImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome',)


class ImovelAdmin(admin.ModelAdmin):
    list_display = ('numero', 'lado', 'tipo', 'habitantes')
    list_filter = ('tipo', 'lado__logradouro', 'lado__quadra__bairro',)
    relfield_style = 'fk-ajax'

admin.site.register(UF, UfAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Bairro, BairroAdmin)
admin.site.register(Quadra, QuadraAdmin)
admin.site.register(Logradouro, LogradouroAdmin)
admin.site.register(TipoImovel, TipoImovelAdmin)
admin.site.register(Imovel, ImovelAdmin)
