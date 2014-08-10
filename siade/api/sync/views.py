from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import SyncSerializer, SyncSerializerForModel


class SyncView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        from siade.imoveis.models import Logradouro, Quadra, LadoQuadra, Imovel
        sync_models = [Logradouro, Quadra, LadoQuadra, Imovel]
        syncData = {}
        for model in sync_models:
            qs = model.objects.all()
            serializerClass = SyncSerializerForModel(model)
            serializer = serializerClass(qs, many=True)
            model_name = model._meta.app_label+'.'+model.__name__
            syncData[model_name] = serializer.data
        return Response(syncData)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.filter_queryset(self.get_queryset()),
            data=request.DATA,
            many=True
        )
        if serializer.is_valid():
            self.object = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
