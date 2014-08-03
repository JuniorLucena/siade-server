# -*- coding: utf-8 -*-
from rest_framework import serializers
from siade.imoveis.models import *
from siade.trabalhos.models import *


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    '''
    Um ModelSerializer que recebe um argumento `fields` que controla quais
    campos serão exibidos.
    '''

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if self.context.has_key('request')
        and self.context['request'].QUERY_PARAMS.has_key('fields'):
            fields = self.context['request'].QUERY_PARAMS.get(
                'fields').split(',')
        else:
            fields = kwargs.get('fields', False)
        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


def SerializerForModel(model_class, *args, **kwargs):
    _fields = kwargs.get('fields', None)
    _depth = kwargs.get('depth', 0)

    class Serializer(DynamicFieldsModelSerializer):

        class Meta:
            model = model_class
            fields = _fields
            depth = _depth

    return Serializer

LadoSerializer = SerializerForModel(LadoQuadra)
QuadraSerializer = SerializerForModel(Quadra)
ImovelSerializer = SerializerForModel(Imovel)
VisitaSerializer = SerializerForModel(Visita)
AgenteSerializer = SerializerForModel(Agente, fields=(
    'first_name', 'last_name', 'username', 'email', 'date_joined', 'last_login'
))
