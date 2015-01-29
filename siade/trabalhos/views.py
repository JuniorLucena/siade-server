from datetime import date
from django.db.models import Count
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import IniciarCicloForm, TrabalhoForm
from .models import Ciclo, Trabalho


def gerenciar_ciclo(request):
    trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())\
        .annotate(total_imoveis=Count('quadras__lados__imoveis'))
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
        form = TrabalhoForm(request.POST, instance=Trabalho(ciclo=Ciclo.atual()))
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect(reverse('ciclo:distribuir_trabalhos'))
    else:
        form = TrabalhoForm(instance=Trabalho(ciclo=Ciclo.atual()))

    trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())\
        .annotate(total_imoveis=Count('quadras__lados__imoveis'))
    context = RequestContext(request, {
        'form': form,
        'trabalhos': trabalhos
    })
    return render_to_response('trabalhos/distribuir_trabalhos.html', context)
