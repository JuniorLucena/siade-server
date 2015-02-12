# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import SyncState


class ModelSyncSerializer(serializers.ModelSerializer):
    sync_changed = serializers.DateTimeField(required=False)
    sync_version = serializers.IntegerField(required=False)
    sync_deleted = serializers.BooleanField(required=False)

    def to_native(self, obj):
        if not obj is None:
            state = SyncState.get_for_object(obj)
            obj.sync_changed = state.changed
            obj.sync_version = state.version
            obj.sync_deleted = state.deleted
        return super(ModelSyncSerializer, self).to_native(obj)

    def save_object(self, obj, **kwargs):
        # Verificar se objeto possui revisão anterior
        if obj.sync_version and obj.id:
            state = SyncState.get_for_object(obj)
            # verificar se o registro possui a mesma versão
            if obj.sync_version == state.version:
                if obj.sync_deleted:
                    return obj.delete()
            else:
                # Essa não, um conflito. A ultima atualização permanece
                if obj.sync_changed < sate.changed:
                    return
        # Salvar o objeto
        return super(ModelSyncSerializer, self).save_object(obj, **kwargs)


def serializer_factory(model_class, base=serializers.ModelSerializer,
                       *args, **kwargs):
    '''
    Retorna um ModelSerializer para um model
    '''
    serializer_name = '%sSerializer' % model_class._meta.object_name
    attrs = kwargs
    attrs.update({'model': model_class})
    meta = type('Meta', (), attrs)
    serializer_class = type(str(serializer_name), (base,),
                            {'Meta': meta})
    return serializer_class

def sync_serializer_factory(model_class, base=ModelSyncSerializer,
                            *args, **kwargs):
    '''
    Retorna um ModelSyncSerializer para um model
    '''
    return serializer_factory(model_class, ModelSyncSerializer, *args, **kwargs)