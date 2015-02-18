from siade.agentes.models import Agente

AgenteDeCampo_permissions = (
    'imoveis.add_imovel',
    'imoveis.change_imovel',
    'imoveis.delete_imovel',
    'imoveis.add_ladoquadra',
    'imoveis.change_ladoquadra',
    'imoveis.delete_ladoquadra',
    'imoveis.add_quadra',
    'imoveis.change_quadra',
    'imoveis.add_logradouro',
    'trabalhos.add_visita',
)

Supervisor_permissions = tuple(AgenteDeCampo_permissions + (
    'imoveis.change_logradouro',
    'imoveis.delete_logradouro',
    'trabalhos.add_trabalho',
    'trabalhos.delete_trabalho',
    'trabalhos.change_trabalho',
    'trabalhos.add_ciclo',
    'trabalhos.change_ciclo',
))

Administrador_permissions = tuple(Supervisor_permissions + (
))

GROUP_PERMISSIONS = {
    Agente.Tipo.AgenteCampo: AgenteDeCampo_permissions,
    Agente.Tipo.Supervisor: Supervisor_permissions,
    Agente.Tipo.Administrador: Administrador_permissions
}
