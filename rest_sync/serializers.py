# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import SyncState


class ModelSyncSerializer(serializers.ModelSerializer):
    sync_changed = serializers.DateTimeField()
    sync_version = serializers.CharField()
    sync_deleted = serializers.BooleanField()

    def __init__(self, *args, **kwargs):
        kwargs.update({'many': True, 'allow_add_remove': True})
        super(ModelSyncSerializer, self).__init__(*args, **kwargs)

    def restore_fields(self, data, files):
        new_data = super(ModelSyncSerializer, self).restore_fields(data, files)
        new_data['id'] = data['id']
        new_data['sync_version'] = data.get('sync_version', '')
        new_data['sync_deleted'] = data.get('sync_deleted', False)
        return new_data

    def to_native(self, obj):
        if obj is not None:
            state = SyncState.get_for_object(obj)
            obj.sync_changed = state.changed
            obj.sync_version = state.version
            obj.sync_deleted = state.deleted
        return super(ModelSyncSerializer, self).to_native(obj)

    def save(self, **kwargs):
        if isinstance(self.object, list):
            [self.save_object(item, **kwargs) for item in self.object]
        return self.object

    def save_object(self, obj, **kwargs):
        # Verificar se objeto possui revisão anterior
        if obj.sync_version:
            state = SyncState.get_for_object(obj)
            # verificar se o registro possui a mesma versão
            if obj.sync_version == state.version:
                if obj.sync_deleted:
                    return obj.delete()
            else:
                # Essa não, um conflito. A ultima atualização permanece
                if obj.sync_changed < state.changed:
                    return
        # Salvar o objeto
        return super(ModelSyncSerializer, self).save_object(obj, **kwargs)


def sync_serializer_factory(model_class, *args, **kwargs):
    '''
    Retorna um ModelFieldsSerializer para um model
    '''
    attrs = kwargs
    attrs.update({'model': model_class})
    meta = type('Meta', (), attrs)
    serializer_class = type(str('Sync%sSerializer' % model_class.__name__),
                            (ModelSyncSerializer,), {'Meta': meta})
    return serializer_class
