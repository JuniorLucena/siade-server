# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..utils import render_html_or_pdf
from ..forms import D1Form


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
    agentes = request.POST.getlist('agentes')
    # aqui vai algum código que vai consultar o dados das visitas do agente na data
    # e colocar no context para serem exibidas no relatório
    context = {}
    return render_html_or_pdf(request, 'relatorios/d1_imprimir.html',
                              context, fmt='pdf')
