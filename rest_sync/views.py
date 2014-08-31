# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.base import ModelBase
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .serializers import ModelSyncSerializer


class ModelSyncView(GenericAPIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated,)
    object = None

    def get(self, request):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not type(request.DATA) is list:
            return Response('Invalid format',
                            status=status.HTTP_400_BAD_REQUEST)

        #self.object_list = self.filter_queryset(self.get_queryset())
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
        self.post_save(self.object)
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


def ModelSyncView_factory(instance, serializer=None):

    class DefaultModelSync(ModelSyncView):
        model = instance
        serializer_class = serializer

    return DefaultModelSync
