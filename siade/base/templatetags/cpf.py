from django import template
from stdnum.br.cpf import format
register = template.Library()


@register.filter()
def cpf_format(value):
    return format(str(value))
