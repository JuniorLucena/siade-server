import xadmin
from .models import *


class AgenteAdmin(object):
    list_display = ('codigo', 'nome', 'sobrenome')
    list_filter = []
    relfield_style = 'fk-ajax'

xadmin.site.register(Agente, AgenteAdmin)
