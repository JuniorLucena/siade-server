from django.core.urlresolvers import reverse
from django import template

register = template.Library()


@register.simple_tag
def object_action(obj, action, *args, **kwargs):
    if not isinstance(obj, basestring):
        obj = obj.__class__.__name__
    return reverse('%s-%s' % (obj.lower(), action),
                   args=args, kwargs=kwargs)


@register.simple_tag
def object_listar(obj, *args, **kwargs):
    return object_action(obj, 'listar', *args, **kwargs)


@register.simple_tag
def object_adicionar(obj, *args, **kwargs):
    return object_action(obj, 'adicionar', *args, **kwargs)


@register.simple_tag
def object_editar(obj, *args, **kwargs):
    return object_action(obj, 'editar', obj.id, *args, **kwargs)


@register.simple_tag
def object_detalhes(obj, *args, **kwargs):
    return object_action(obj, 'detalhes', obj.id, *args, **kwargs)


@register.simple_tag
def object_excluir(obj, *args, **kwargs):
    return object_action(obj, 'excluir', obj.id, *args, **kwargs)
