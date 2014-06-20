from django.utils.translation import gettext as _
import xadmin
from xadmin.plugins.batch import BatchChangeAction
from .models import *

class UfAdmin(object):
	list_display = ('nome', 'sigla')
	search_fields = ('nome',)

class MunicipioAdmin(object):
	list_display = ('nome', 'uf')
	search_fields = ('nome',)
	list_filter = ('uf',)

class BairroAdmin(object):
	list_display = ('nome', 'municipio')
	search_fields = ('nome',)
	list_filter = ('municipio',)

class LadoQuadraInline(object):
	model = LadoQuadra
	style = 'table'
	list_display = ('logradouro')
	verbose_name_plural = 'lados'

class QuadraAdmin(object):
	list_display = ('numero', 'bairro')
	list_filter = ('bairro',)
	ordering = ('bairro__nome', 'numero')
	actions = (BatchChangeAction,)
	batch_fields = ('bairro',)
	inlines = (LadoQuadraInline,)

class LogradouroAdmin(object):
	list_display = ('nome', 'municipio')
	search_fields = ('nome',)
	list_filter = ('municipio',)

class TipoImovelAdmin(object):
	list_display = ('nome', 'sigla')
	search_fields = ('nome',)

class ImovelAdmin(object):
	list_display = ('numero', 'tipo', 'lado', 'habitantes')
	list_filter = ('tipo', 'lado__logradouro', 'lado__quadra__bairro',)
	actions = (BatchChangeAction,)
	batch_fields = ('lado',)

xadmin.site.register(UF, UfAdmin)
xadmin.site.register(Municipio, MunicipioAdmin)
xadmin.site.register(Bairro, BairroAdmin)
xadmin.site.register(Quadra, QuadraAdmin)
xadmin.site.register(Logradouro, LogradouroAdmin)
xadmin.site.register(TipoImovel, TipoImovelAdmin)
xadmin.site.register(Imovel, ImovelAdmin)