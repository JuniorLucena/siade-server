# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from rest_framework import serializers


class ModelSyncSerializer(serializers.ModelSerializer):
    sync_changed = serializers.DateTimeField(required=False)
    sync_version = serializers.IntegerField(required=False)
    sync_deleted = serializers.BooleanField(required=False)

    def to_native(self, obj):
        # set sync attributes if object has history
        if hasattr(obj, 'history'):
            last = obj.history.first()
            if last is not None:
                obj.sync_changed = last.history_date
                obj.sync_version = last.history_id
                obj.sync_deleted = last.history_type == '-'

        return super(ModelSyncSerializer, self).to_native(obj)

    def from_native(self, data, files=None):
        #if data is not None:
            #if data.get('sync_version', None) is None:
            #    data.pop('id', None)
        return super(ModelSyncSerializer, self).from_native(data, files)

    def restore_object(self, attrs, instance=None):
        sync_changed = attrs.get('sync_changed', None)
        if instance is not None and sync_changed:
            instance._history_date = sync_changed
        return super(ModelSyncSerializer, self).restore_object(attrs, instance)

    def save_object(self, obj, **kwargs):
        if obj.sync_version and obj.id:
            # check if is same version of record
            if obj.sync_version == obj.history.first().history_id:
                if obj.sync_deleted:
                    return obj.delete()
            else:
                # oh no! it's a conflict. The last update wins
                if obj.sync_changed < obj.history.first().history_date:
                    return
        return super(ModelSyncSerializer, self).save_object(obj, **kwargs)


def ModelSyncSerializer_factory(model_class, *args, **kwargs):
    '''
    Retorna um ModelSyncSerializer para um model
    '''
    _fields = kwargs.get('fields', None)

    class Serializer(ModelSyncSerializer):

        class Meta:
            model = model_class
            fields = _fields

    return Serializer
