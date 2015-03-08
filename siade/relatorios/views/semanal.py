# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.shortcuts import render
from siade.agentes.models import Agente
from siade.imoveis.models import Bairro, Imovel
from siade.trabalhos.models import Ciclo, Visita
from django.db.models import Count, Sum
from ..utils import render_html_or_pdf, to_djchoices_totals
from ..forms import D7Form


@login_required
def form(request):
    if request.method == 'POST':
        form = D7Form(request.POST)
        if form.is_valid():
            # ao invés de redicionar executar a view
            return imprimir(request)
    else:
        form = D7Form()
    return render(request, 'relatorios/d7_form.html', {'form': form})


def imprimir(request):
    semana = int(request.POST.get('semana'))
    agentes = request.POST.getlist('agentes')
    ciclo = Ciclo.atual()
    data_inicio = ciclo.data_inicio + timedelta(days=(semana-1)*7)
    data_fim = data_inicio + timedelta(days=semana*7)
    visitas = Visita.objects.filter(data__gt=data_inicio, data__lt=data_fim)
    visitas_por_agente = []

    for agente in agentes:
        visitas_por_bairro = []
        visitas_do_agente = visitas.filter(agente=agente)
        bairros_ids = set(visitas_do_agente.values_list(
            'imovel__lado__quadra__bairro', flat=True))
        bairros = Bairro.objects.filter(id__in=bairros_ids)

        for bairro in bairros:
            visitas_do_bairro = visitas_do_agente.filter(
                imovel__lado__quadra__bairro=bairro)

            # inicia dict totais
            totais = {
                'bairro': bairro,
            }

            # Agregados de vários campos
            totais.update(visitas_do_bairro.aggregate(
                a1=Sum('A1'), a2=Sum('A2'), b=Sum('B'), c=Sum('C'),
                d1=Sum('D1'), d2=Sum('D2'), e=Sum('E'), tubitos=Sum('tubitos'),
                depositos_eliminados=Sum('depositos_eliminados'),
                deposito_tratados=Sum('depositos_tratados'),
                qtd_larvicida=Sum('qtd_larvicida'),
                imovel_tratado=Count('imovel_tratado'),
                imovel_inspecionado=Count('imovel_inspecionado'),
                informados=Count('pk')
            ))

            #
            totais['ponto_estrategico'] = visitas_do_bairro.filter(
                imovel__ponto_estrategico=True).count()

            # contar imóveis por tipo
            imoveis_por_tipo = to_djchoices_totals(
                visitas_do_bairro, 'imovel__tipo', Count('imovel'),
                Imovel.Tipo, 'imovel_')
            totais.update(imoveis_por_tipo)

            # Pegar total de imóveis
            totais['imoveis'] = visitas_do_bairro\
                .values('imovel').distinct().count()

            # Pegar total de quadras
            totais['quadras'] = visitas_do_bairro\
                .values('imovel__lado__quadra').distinct().count()

            # contar visitas por tipo
            visitas_por_tipo = to_djchoices_totals(
                visitas_do_bairro, 'tipo', Count('pk'),
                Visita.Tipo, 'tipo_')
            totais.update(visitas_por_tipo)

            # contar visitas por pendencia
            visitas_por_pendencia = to_djchoices_totals(
                visitas_do_bairro, 'pendencia', Count('pk'),
                Visita.Pendencia, 'pendencia_')
            totais.update(visitas_por_pendencia)

            # pegar quantidade de amostras
            qtd_amostras = 0
            for visita in visitas_do_bairro:
                qtd_amostras += (visita.amostra_final or 0)-(visita.amostra_inicial or 0)
            totais['amostras'] = qtd_amostras

            visitas_por_bairro += [totais]

        visitas_por_agente += [{
            'agente': Agente.objects.get(pk=agente),
            'bairros': visitas_por_bairro
        }]

    context = {
        'ciclo': ciclo,
        'totais_por_agente': visitas_por_agente,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    }
    return render_html_or_pdf(request, 'relatorios/d7_imprimir.html',
                              context, fmt='html')
