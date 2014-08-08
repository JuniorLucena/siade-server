# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers
from siade.imoveis.models import *
from siade.trabalhos.models import *


class FieldsModelSerializer(serializers.ModelSerializer):
    '''
    Um ModelSerializer que recebe um argumento `fields` que controla quais
    campos serão exibidos.
    '''
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(FieldsModelSerializer, self).__init__(*args, **kwargs)

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


def SerializerForModel(model_class, *args, **kwargs):
    '''
    Retorna um FieldsModelSerializer para um model
    '''
    _fields = kwargs.get('fields', None)
    _depth = kwargs.get('depth', 0)

    class Serializer(FieldsModelSerializer):

        class Meta:
            model = model_class
            fields = _fields
            depth = _depth

    return Serializer


class SyncSerializer(serializers.ModelSerializer):
    sync_changed = serializers.DateTimeField(read_only=True)
    sync_version = serializers.IntegerField(read_only=True)
    sync_deleted = serializers.BooleanField()

    def to_native(self, obj):
        last = obj.history.first()
        obj.sync_changed = last.history_date
        obj.sync_version = last.history_id
        obj.sync_deleted = last.history_type == '-'
        return super(SyncSerializer, self).to_native(obj)


def SyncSerializerForModel(model_class, *args, **kwargs):
    '''
    Retorna um SyncSerializer para um model
    '''
    _fields = kwargs.get('fields', None)
    _depth = kwargs.get('depth', 0)

    class Serializer(SyncSerializer):

        class Meta:
            model = model_class
            fields = _fields
            depth = _depth

    return Serializer


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'username',
                  'email', 'groups', 'user_permissions')

LadoSerializer = SerializerForModel(LadoQuadra)
QuadraSerializer = SerializerForModel(Quadra)
ImovelSerializer = SerializerForModel(Imovel)
VisitaSerializer = SerializerForModel(Visita)
AgenteSerializer = SerializerForModel(Agente, fields=(
    'first_name', 'last_name', 'username', 'email', 'date_joined', 'last_login'
))
