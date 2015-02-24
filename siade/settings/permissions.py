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
    'imoveis.change_logradouro',
    'imoveis.change_bairro',
    'trabalhos.add_visita',
)

Supervisor_permissions = tuple(AgenteDeCampo_permissions + (
    'agentes.add_agente',
    'agentes.change_agente',
    'agentes.delete_agente',
    'imoveis.add_bairro',
    'imoveis.delete_bairro',
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
