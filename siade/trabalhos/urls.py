from django.conf.urls import url, patterns
from .views import *


urlpatterns = patterns(
    '',
    url(r'^iniciar_ciclo/$', iniciar_ciclo, name='iniciar_ciclo'),
    url(r'^distribuir_trabalhos/$', distribuir_trabalhos,
        name='distribuir_trabalhos'),
)
