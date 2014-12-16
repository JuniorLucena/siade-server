from .models import Ciclo


def ciclo_atual(request):
    return {'ciclo_atual': Ciclo.atual()}
