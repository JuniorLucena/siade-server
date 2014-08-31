# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers


class ModelFieldsSerializer(serializers.ModelSerializer):
    '''
    Um ModelSerializer que recebe um argumento `fields` que controla quais
    campos serão exibidos.
    '''
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ModelFieldsSerializer, self).__init__(*args, **kwargs)

        request = self.context.get('request', None)
        if request:
            fields = request.QUERY_PARAMS.get('fields', None)
            if fields:
                fields = fields.split(',')
        else:
            fields = None
        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


def ModelFieldsSerializer_factory(model_class, *args, **kwargs):
    '''
    Retorna um ModelFieldsSerializer para um model
    '''
    _fields = kwargs.get('fields', None)
    _depth = kwargs.get('depth', 0)

    class Serializer(ModelFieldsSerializer):

        class Meta:
            model = model_class
            fields = _fields
            depth = _depth

    return Serializer
