from django.conf.urls import url, patterns
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import serializer_factory
from siade.agentes.models import Agente


class AgenteView(RetrieveAPIView):
    ''' Retornar dados do agente atualmente logado no sistema '''

    model_class = Agente
    serializer_class = serializer_factory(
        Agente, exclude=('password', 'last_login', 'is_superuser',
                         'ativo', 'groups', 'user_permissions'))
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


urls = patterns(
    '',
    url(r'^agente/$', AgenteView.as_view(), name='agente'),
)
