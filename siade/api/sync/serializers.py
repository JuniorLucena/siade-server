# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import serializers


class SyncSerializer(serializers.ModelSerializer):
    sync_changed = serializers.DateTimeField(read_only=True)
    sync_version = serializers.IntegerField(read_only=True)
    sync_deleted = serializers.BooleanField()

    def to_native(self, obj):
        # set sync attributes if object has history
        try:
            last = obj.history.first()
            obj.sync_changed = last.history_date
            obj.sync_version = last.history_id
            obj.sync_deleted = last.history_type == '-'
        except AttributeError:
            pass
        return super(SyncSerializer, self).to_native(obj)

    def save_object(obj, **kwargs):
        print obj.sync_version
        if obj.sync_deleted:
            obj.delete()
        else:
            obj.save()


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
