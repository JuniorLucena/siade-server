from datetime import date
from django.db.models import Count
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import IniciarCicloForm, TrabalhoForm
from .models import Ciclo
from siade.agentes.models import Agente


def gerenciar_ciclo(request):
    agentes = Agente.objects.select_related('trabalhos').only('nome')\
        .filter(tipo=Agente.Tipo.AgenteCampo)\
        .annotate(total_imoveis=Count('trabalhos__quadra__lados__imoveis'))

    vistas_agentes = dict(Agente.objects.annotate(
        total=Count('visitas__imovel')).values_list('id', 'total'))

    for a in agentes:
        a.total_visitas = vistas_agentes[a.id]
        percentual = float(a.total_visitas / float(a.total_imoveis))
        print percentual
        a.percentual = int(round(percentual * 100))

    context = {
        'agentes': agentes
    }
    return render(request, 'trabalhos/gerenciar_ciclo.html', context)


def iniciar_ciclo(request):
    if request.method == 'POST':
        form = IniciarCicloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('ciclo:distribuir_trabalhos'))
    else:
        form = IniciarCicloForm()

    context = RequestContext(request, {'form': form})
    return render_to_response('trabalhos/iniciar_ciclo.html', context)


def encerrar_ciclo(request):
    ciclo = Ciclo.atual()
    if request.method == 'POST':
        ciclo.fechado_em = date.today()
        ciclo.save()
        return redirect(reverse('ciclo:gerenciar'))
    else:
        context = RequestContext(request, {
            'ciclo': ciclo,
        })
        return render_to_response('trabalhos/encerrar_ciclo.html', context)


def distribuir_trabalhos(request):
    agente_id = request.GET.get('agente') or request.POST.get('agente')
    if request.method == 'POST':
        form = TrabalhoForm(agente_id, request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('ciclo:distribuir_trabalhos'))
    else:
        form = TrabalhoForm(agente_id)

    agentes = Agente.objects.select_related('trabalhos').only('nome')\
        .filter(tipo=Agente.Tipo.AgenteCampo)\
        .annotate(total_imoveis=Count('trabalhos__quadra__lados__imoveis'))

    context = {
        'form': form,
        'agentes': agentes,
    }
    return render(request, 'trabalhos/distribuir_trabalhos.html', context)
