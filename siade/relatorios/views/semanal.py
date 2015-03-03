# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..utils import render_html_or_pdf
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
    data_inicio = request.POST.get('data_inicio')
    data_fim = request.POST.get('data_fim')
    agentes = request.POST.getlist('agentes')
    # aqui vai algum código que vai consultar o dados das visitas do agente no
    # intevalo de datas e colocar no context para serem exibidas no relatório
    context = {}
    return render_html_or_pdf(request, 'relatorios/d7_imprimir.html',
                              context, fmt='html')
