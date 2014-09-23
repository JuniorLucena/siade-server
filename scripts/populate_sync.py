from siade.imoveis.models import *
from siade.trabalhos.models import *
from rest_sync.models import SyncState


def run():
    for model in [Logradouro, Quadra, LadoQuadra, Imovel, Trabalho, Visita]:
        for item in model.objects.all():
            SyncState.get_for_object(item)
