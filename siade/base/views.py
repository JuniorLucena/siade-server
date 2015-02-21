from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import shortuuid


def qrcode(request):
    qtd = int(request.GET.get('qtd', 10))
    qrcodes = [shortuuid.uuid() for i in range(qtd)]
    return render(request, 'qrcode.html', {'qrcodes': qrcodes})


@login_required
def home(request):
    return render(request, 'home.html', {})
