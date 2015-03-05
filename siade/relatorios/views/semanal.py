# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.shortcuts import render
from ..utils import render_html_or_pdf
from ..forms import D7Form
from siade.agentes.models import Agente
from siade.imoveis.models import Bairro
from siade.trabalhos.models import Ciclo, Visita
from django.db.models import Count, Sum


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
    data_fim = ciclo.data_fim + timedelta(days=semana*7)

    print data_inicio, data_fim
      
    visitas = Visita.objects.filter(data__gt=data_inicio,data__lt=data_fim)

    visitas_agentes = []



    for agente in agentes:
        bairros = set(visitas.filter(agente=agente).values_list('imovel__lado__quadra__bairro', flat=True))

        visitas_bairros = []

        filter_visitas = visitas.filter(agente=agente)

        for bairro in bairros:
            qtd_amostras = 0
            for visita in filter_visitas.filter(imovel__lado__quadra__bairro=bairro):
                qtd_amostras += (visita.amostra_final or 0)-(visita.amostra_inicial or 0)

            visita_agente = {
                'bairro': Bairro.objects.get(pk=bairro),
                'num_informados' : filter_visitas.count(),
                'qtd_amostras' : qtd_amostras,
            }

            v = [
            filter_visitas.filter(imovel__tipo=2).aggregate(num_comercio=Count('imovel')),
            filter_visitas.filter(imovel__tipo=1).aggregate(num_residencia=Count('imovel')),
            filter_visitas.filter(imovel__tipo=3).aggregate(num_TB=Count('imovel')),
            filter_visitas.filter(imovel__tipo=4).aggregate(num_outros=Count('imovel')),
            filter_visitas.filter(imovel__ponto_estrategico=True).aggregate(num_PE=Count('imovel')),
            filter_visitas.aggregate(num_total=Count('imovel')),
            filter_visitas.distinct().aggregate(num_quadra=Count('imovel__lado__quadra')),

            filter_visitas.filter(pendencia=3).aggregate(recusada=Count('pendencia')),
            filter_visitas.filter(pendencia=2).aggregate(fechada=Count('pendencia')),
            filter_visitas.filter(tipo=2).aggregate(recuperada=Count('tipo')),

            filter_visitas.filter(imovel_tratado=True).aggregate(tratado=Count('imovel_tratado')),
            filter_visitas.filter(imovel_inspecionado=True).aggregate(inspecionado=Count('imovel_inspecionado')),
        
            filter_visitas.aggregate(eliminados=Sum('depositos_eliminados')),
            filter_visitas.aggregate(tipo_larvicida=Sum('larvicida')),
            filter_visitas.aggregate(qtd_larvicida=Sum('qtd_larvicida')),
            filter_visitas.aggregate(qtd_deposito_tratados=Sum('depositos_tratados')),

            filter_visitas.aggregate(a1=Sum('A1')),
            filter_visitas.aggregate(a2=Sum('A2')),
            filter_visitas.aggregate(b=Sum('B')),
            filter_visitas.aggregate(c=Sum('C')),
            filter_visitas.aggregate(d1=Sum('D1')),
            filter_visitas.aggregate(d2=Sum('D2')),
            filter_visitas.aggregate(e=Sum('E')),
            filter_visitas.aggregate(amostra_inicial=Sum('amostra_inicial')),
            filter_visitas.aggregate(amostra_final=Sum('amostra_final')),
            filter_visitas.aggregate(tubitos=Sum('tubitos')),   
            ]

            for d in v:
                visita_agente.update(d)        

            visitas_bairros.append(visita_agente)

        visitas_agentes += [{
            'agente': Agente.objects.get(pk=agente),
            'ciclo': Ciclo.atual(),
            'bairros': visitas_bairros
        }]


    context = {
        'visitas_agentes':visitas_agentes,
        'data_inicio':data_inicio,
        'data_fim':data_fim,
    }
    return render_html_or_pdf(request, 'relatorios/d7_imprimir.html',
                              context, fmt='html')
