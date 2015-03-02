from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import shortuuid
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render, get_object_or_404
from siade.agentes.models import Agente
from siade.imoveis.views import bairro
from siade.trabalhos.views import *

def qrcode(request):
    qtd = int(request.GET.get('qtd', 10))
    qrcodes = [shortuuid.uuid() for i in range(qtd)]
    return render(request, 'qrcode.html', {'qrcodes': qrcodes})

def gerar_code(request):
	return render(request, 'qrcode_form.html', {})

@login_required
def home(request):
	
	if request.user.tipo == Agente.Tipo.AgenteCampo:
		return redirect(reverse('imoveis:bairro:listar'))
	elif request.user.tipo == Agente.Tipo.Supervisor:
		return redirect(reverse('ciclo:gerenciar'))
	else:
		return render(request, 'home.html', {})

	