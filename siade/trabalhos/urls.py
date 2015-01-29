from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns(
    '',
    url(r'^iniciar/$', iniciar_ciclo, name='iniciar'),
    url(r'^encerrar/$', encerrar_ciclo, name='encerrar'),
    url(r'^gerenciar/$', gerenciar_ciclo, name='gerenciar'),
    url(r'^distribuir_trabalhos/$', distribuir_trabalhos,
        name='distribuir_trabalhos'),
)
