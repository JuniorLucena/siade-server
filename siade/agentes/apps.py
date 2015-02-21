from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .management import atualizar_grupos


class AgentesConfig(AppConfig):
    name = 'siade.agentes'

    def ready(self):
        post_migrate.connect(atualizar_grupos,
                             dispatch_uid="siade.agentes.atualizar_grupos")
