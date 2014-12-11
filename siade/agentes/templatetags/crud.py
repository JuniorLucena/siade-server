from django import template
register = template.Library()


@register.simple_tag
def verbose_name(object):
    return object._meta.verbose_name


@register.simple_tag
def verbose_name_plural(object):
    return object._meta.verbose_name_plural
