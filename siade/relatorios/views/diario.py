# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..utils import render_html_or_pdf
from datetime import datetime
from ..forms import D1Form
from siade.agentes.models import Agente
from siade.imoveis.models import Bairro
from siade.trabalhos.models import Ciclo, Visita


@login_required
def form(request):
    if request.method == 'POST':
        form = D1Form(request.POST)
        if form.is_valid():
            # ao invés de redicionar executar a view
            return imprimir(request)
    else:
        form = D1Form()
    return render(request, 'relatorios/d1_form.html', {'form': form})

def imprimir(request):
    data = request.POST.get('data')
    data = datetime.strptime(data, '%d/%m/%Y')

    agentes = request.POST.getlist('agentes')

    visitas = Visita.objects.filter(data=data)

    visitas_agentes = []

    for agente in agentes:
        bairros = set(visitas.filter(agente=agente).values_list('imovel__lado__quadra__bairro', flat=True))

        visitas_bairros = []

        for bairro in bairros:
            visita_agente = {
                'bairro': Bairro.objects.get(pk=bairro),
                'visitas': visitas.filter(agente=agente), 
            }
            visitas_bairros.append(visita_agente)

        visitas_agentes += [{
            'data': data,
            'agente': Agente.objects.get(pk=agente),
            'ciclo': Ciclo.atual(),
            'bairros': visitas_bairros,
        }]

    context = {
        'visitas_agentes' : visitas_agentes,
    }
    return render_html_or_pdf(request, 'relatorios/d1_imprimir.html',
                              context, fmt='html')
