from datetime import date
from django.db.models import Count
from django.shortcuts import (render_to_response, redirect,
                              get_object_or_404)
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import IniciarCicloForm, TrabalhoForm
from .models import Ciclo, Trabalho
from siade.agentes.models import Agente


def gerenciar_ciclo(request):
    #trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())\
        #.annotate(total_imoveis=Count('quadras__lados__imoveis'))
    trabalhos = None
    context = RequestContext(request, {
        'trabalhos': trabalhos
    })
    return render_to_response('trabalhos/gerenciar_ciclo.html', context)


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
    if request.method == 'POST':
        form = TrabalhoForm(request.POST,
                            instance=Trabalho(ciclo=Ciclo.atual()))
        if form.is_valid():
            form.save()
            return redirect(reverse('ciclo:distribuir_trabalhos'))
    else:
        form = TrabalhoForm(instance=Trabalho(ciclo=Ciclo.atual()))

    agentes = Agente.objects.filter(
        trabalhos__ciclo=Ciclo.atual()).annotate(
        total_imoveis=Count('trabalhos__quadra__lados__imoveis'))

    context = RequestContext(request, {
        'form': form,
        'agentes': agentes
    })
    return render_to_response('trabalhos/distribuir_trabalhos.html', context)
