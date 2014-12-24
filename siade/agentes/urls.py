from django.conf.urls import url, include
from .views import agente

urlpatterns = [
    url(r'^agente/', include(agente.urls))
]
