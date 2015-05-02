# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import SyncState


class ListModelSyncSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        instance_map = {o.id: o for o in instance}
        data_map = {d['id']: d for d in validated_data}
        ret = []

        # Perform creations and updates
        for pk, data in data_map.items():
            instance = instance_map.get(pk)
            if data.get('sync_deleted', False):
                if instance is not None:
                    instance.delete()
            else:
                if instance is None:
                    ret.append(self.child.create(data))
                else:
                    ret.append(self.child.update(instance, data))

        return ret


class ModelSyncSerializer(serializers.ModelSerializer):
    sync_changed = serializers.DateTimeField()
    sync_version = serializers.CharField(allow_blank=True, read_only=True)
    sync_deleted = serializers.BooleanField()

    def to_internal_value(self, data):
        native_data = super(ModelSyncSerializer, self).to_internal_value(data)
        native_data['id'] = data.get('id')
        return native_data

    def to_representation(self, instance):
        if instance is not None:
            state = SyncState.get_for_object(instance)
            instance.sync_changed = state.changed
            instance.sync_version = state.version
            instance.sync_deleted = state.deleted

        data = super(ModelSyncSerializer, self).to_representation(instance)
        return data

    def create(self, validated_data):
        validated_data = ModelSyncSerializer.remove_sync_data(validated_data)
        return super(ModelSyncSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data = ModelSyncSerializer.remove_sync_data(validated_data)
        return super(ModelSyncSerializer, self).update(instance,
                                                       validated_data)

    @classmethod
    def many_init(cls, *args, **kwargs):
        kwargs['child'] = cls()
        return ListModelSyncSerializer(*args, **kwargs)

    @classmethod
    def remove_sync_data(cls, data):
        return {k: v for k, v in data.items() if k not in (
            'sync_version', 'sync_changed', 'sync_deleted')}


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
