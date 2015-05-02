# -*- coding: utf-8 -*-
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import sync_serializer_factory
from .models import SyncState


def datetime_from_string(s):
    from dateutil.parser import parse
    try:
        val = datetime.fromtimestamp(float(s))
    except ValueError:
        val = parse(s)
    return val


class ModelSyncView(GenericAPIView):
    def filter_queryset(self, queryset):
        since_param = self.request.GET.get('from') or self.request.GET.get('since')
        if since_param is None:
            return queryset

        self.request.is_filtered = True
        since = datetime_from_string(since_param)
        object_type = ContentType.objects.get_for_model(queryset.model)
        time_range = (since, datetime.now())
        obj_qs = SyncState.objects.filter(object_type=object_type,
                                          changed__range=time_range)
        obj_ids = obj_qs.values_list('object_id', flat=True)
        queryset = queryset.filter(id__in=obj_ids)
        return queryset

    def get(self, request, format=None):
        object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(object_list, many=True)
        return Response(serializer.data)

    def post(self, request, fmt=None):
        if not type(request.DATA) is list:
            return Response('Post Data must be a list of objects',
                            status=status.HTTP_400_BAD_REQUEST)

        object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(object_list, many=True,
                                         data=request.DATA)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        self.object_list = serializer.save()

        if getattr(request, 'is_filtered'):
            return self.get(request, fmt)

        return Response({'status': 'ok'})

    def get_serializer_class(self):
        if self.serializer_class is not None:
            return self.serializer_class

        model_class = self.get_queryset().model
        self.serializer_class = sync_serializer_factory(model_class)
        return self.serializer_class


def ModelSyncView_factory(model_class, serializer=None):
    view_name = '%sSyncView' % model_class._meta.object_name
    attrs = {'model': model_class, 'serializer_class': serializer}
    model_sync_view = type(str(view_name), (ModelSyncView,), attrs)
    return model_sync_view
