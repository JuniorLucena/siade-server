# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_sync.serializers import ModelSyncSerializer
from siade.imoveis.models import Imovel
from siade.trabalhos.models import Ciclo


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


def serializer_factory(model_class, base=ModelFieldsSerializer,
                       *args, **kwargs):
    '''
    Retorna um ModelFieldsSerializer para um model
    '''
    serializer_name = '%sSerializer' % model_class._meta.object_name
    attrs = kwargs
    attrs.update({'model': model_class})
    meta = type('Meta', (), attrs)
    serializer_class = type(str(serializer_name), (base,),
                            {'Meta': meta})
    return serializer_class


class ImovelSyncSerializer(ModelSyncSerializer):
    pendencia = serializers.IntegerField(read_only=True)

    def to_native(self, obj):
        if not obj is None:
            obj.pendencia = 0

            if hasattr(obj, 'visitas'):
                visita = obj.visitas.first()
                if visita is not None:
                    obj.pendencia = visita.pendencia

        return super(ImovelSyncSerializer, self).to_native(obj)

    class Meta:
        model = Imovel
