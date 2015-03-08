# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from siade.trabalhos.models import Visita
from ..forms import D1Form
from ..utils import render_html_or_pdf


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
    data = datetime.strptime(request.POST.get('data'), '%d/%m/%Y').date
    agentes = request.POST.getlist('agentes')
    visitas = Visita.objects.filter(data=data)
    context = {
        'visitas': visitas.filter(agente__in=agentes)
                          .order_by('agente', 'imovel__lado__quadra__bairro'),
        'data': data,
    }
    return render_html_or_pdf(request, 'relatorios/d1_imprimir.html',
                              context, fmt='html')
