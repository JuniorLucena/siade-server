# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .serializers import ModelSyncSerializer, ModelSyncSerializer_factory
from .models import SyncState


def datetime_from_string(s):
    from dateutil.parser import parse
    try:
        val = datetime.fromtimestamp(float(s))
    except ValueError:
        val = parse(s)
    return val


class ModelSyncView(GenericAPIView):
    object = None

    def filter_queryset(self, queryset):
        sync_from = self.request.GET.get('from')
        if sync_from is None:
            return queryset

        sync_time = datetime_from_string(sync_from)
        object_type = ContentType.objects.get_for_model(queryset.model)
        obj_ids = SyncState.objects.filter(object_type=object_type,
                                           changed__range=(sync_time, datetime.now())) \
                                   .values_list('object_id', flat=True)
        queryset = queryset.filter(id__in=obj_ids)
        print queryset.query
        return queryset

    def get(self, request):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not type(request.DATA) is list:
            return Response('Invalid format',
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(many=True,
                                         data=request.DATA,
                                         files=request.FILES)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            self.pre_save(serializer.object)
        except ValidationError as err:
            return Response(err.message_dict,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        self.post_save(serializer.object)
        return self.get(request)

    def get_serializer(self, instance=None, data=None, files=None, many=False,
                       partial=False, allow_add_remove=False):
        serializer_class = self.get_serializer_class()
        context = self.get_serializer_context()
        return serializer_class(instance, data=data, files=files,
                                many=many, partial=partial,
                                allow_add_remove=allow_add_remove,
                                context=context)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if serializer_class is not None:
            return serializer_class

        model_class = self.get_queryset().model

        class DefaultSerializer(ModelSyncSerializer):
            class Meta:
                model = model_class
        return DefaultSerializer

    def get_object(self):
        return self.get_queryset()


def ModelSyncView_factory(model_class, serializer=None):
    serializer_name = '%sSyncView' % model_class._meta.object_name
    attrs = {'model': model_class, 'serializer_class': serializer}
    model_sync_view = type(str(serializer_name), (ModelSyncView,), attrs)
    return model_sync_view
