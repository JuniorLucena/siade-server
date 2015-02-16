from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
import shortuuid


def qrcode(request):
    qtd = int(request.GET.get('qtd', 10))
    qrcodes = [shortuuid.uuid() for i in range(qtd)]
    return render_to_response("qrcode.html", {'qrcodes': qrcodes})


@login_required
def home(request):
    return TemplateResponse(request, "home.html", {})
