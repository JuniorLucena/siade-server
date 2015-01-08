from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import IniciarCicloForm, TrabalhoForm
from .models import Ciclo, Trabalho


def iniciar_ciclo(request):
    if request.method == 'POST':
        form = IniciarCicloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('trabalhos:distribuir_trabalhos'))
    else:
        form = IniciarCicloForm()

    context = RequestContext(request, {'form': form})
    return render_to_response('trabalhos/iniciar_ciclo.html', context)


def distribuir_trabalhos(request):
    if request.method == 'POST':
        form = TrabalhoForm(request.POST)
        if form.is_valid():
            instance = form.save(False)
            instance.ciclo = Ciclo.atual()
            instance.save()
            return redirect(reverse('trabalhos:distribuir_trabalhos'))
    else:
        form = TrabalhoForm()

    trabalhos = Trabalho.objects.filter(ciclo=Ciclo.atual())\
                                .order_by('agente__nome')
    context = RequestContext(request, {'form': form, 'trabalhos': trabalhos})
    return render_to_response('trabalhos/distribuir_trabalhos.html', context)
