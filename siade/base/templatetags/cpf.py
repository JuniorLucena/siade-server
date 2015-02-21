from django import template
from stdnum.br import cpf
register = template.Library()


@register.filter()
def cpf_format(value):
    return cpf.format(str(value).zfill(11))
