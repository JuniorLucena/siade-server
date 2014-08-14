from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import model_syncserializer_factory


def get_model_or_404(app_name, model_name):
    """
    Attempt to get a model from the ``AppCache``
    and raise ``Http404`` if it cannot be found
    """
    from django.db.models import get_model
    from django.http import Http404

    sync_enabled_models = getattr(settings, 'REST_SYNC_MODELS', [])

    if '%s.%s' % (app_name, model_name) in sync_enabled_models:
        model_class = get_model(app_name, model_name)
        if not model_class is None:
            return model_class

    raise Http404("This model does not exist!")


class SyncView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        app_name = kwargs.get('app', None)
        model_name = kwargs.get('model', None)
        model = get_model_or_404(app_name, model_name)

        qs = model.objects.all()
        serializerClass = model_syncserializer_factory(model)
        serializer = serializerClass(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if not type(request.DATA) is dict:
            return Response('Invalid format',
                            status=status.HTTP_400_BAD_REQUEST)

        app_name = kwargs.get('app', None)
        model_name = kwargs.get('model', None)
        model = get_model_or_404(app_name, model_name)
        serializerClass = model_syncserializer_factory(model)
        serializer = serializerClass(data=request.DATA, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response('Update successful', status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
