from django.conf import settings
from django.db.models.loading import get_model
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import model_syncserializer_factory


class SyncView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        REST_SYNC_MODELS = getattr(settings, 'REST_SYNC_MODELS', [])
        syncData = {}
        for model_name in REST_SYNC_MODELS:
            model = get_model(*model_name.split('.', 1))
            qs = model.objects.all()
            serializerClass = model_syncserializer_factory(model)
            serializer = serializerClass(qs, many=True)
            syncData[model_name] = serializer.data
        return Response(syncData)

    def post(self, request, *args, **kwargs):
        REST_SYNC_MODELS = getattr(settings, 'REST_SYNC_MODELS', [])
        if not type(request.DATA) is dict:
            return Response('Invalid format',
                            status=status.HTTP_400_BAD_REQUEST)

        for model_name, model_data in request.DATA.items():
            if not model_name in REST_SYNC_MODELS:
                continue
            model = get_model(*model_name.split('.', 1))
            serializerClass = model_syncserializer_factory(model)
            serializer = serializerClass(data=model_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
