# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Group, Permission
from siade.agentes.models import Agente
from siade.settings.permissions import GROUP_PERMISSIONS


def permission_names_to_objects(names):
    '''
    Given an iterable of permission names (e.g. 'app_label.add_model'),
    return an iterable of Permission objects for them.
    The permission must already exist, because a permission name is not enough
    information to create a new permission.
    '''
    result = []
    for name in names:
        app_label, codename = name.split(".", 1)
        # Is that enough to be unique? Hope so
        try:
            result.append(Permission.objects.get(
                content_type__app_label=app_label, codename=codename))
        except Permission.DoesNotExist:
            raise Exception(
                'No such permission: %s, %s' % (app_label, codename))

    return result


def create_or_update_groups(*args, **kwargs):
    for val, name in Agente.Tipo.choices:
        group, c = Group.objects.get_or_create(name=name)
        if val in GROUP_PERMISSIONS.keys():
            perms = permission_names_to_objects(GROUP_PERMISSIONS.get(val))
            group.permissions = perms
