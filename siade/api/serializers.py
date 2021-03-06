# -*- coding: utf-8 -*-
from rest_framework import serializers


class ModelFieldsSerializer(serializers.ModelSerializer):
    '''
    Um ModelSerializer que recebe um argumento `fields` que controla quais
    campos serão exibidos.
    '''
    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        fields = None
        request = kwargs['context'].get('request', None)
        if request:
            fields = request.QUERY_PARAMS.get('fields')
            self.Meta.fields = fields.split(',') if fields else None
            self.Meta.depth = int(request.QUERY_PARAMS.get('depth', 0))

        super(ModelFieldsSerializer, self).__init__(*args, **kwargs)


def serializer_factory(model_class, base=serializers.ModelSerializer,
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
