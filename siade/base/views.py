from django.shortcuts import render_to_response
import shortuuid


def qrcode(request):
    qtd = int(request.GET.get('qtd', 10))
    qrcodes = [shortuuid.uuid() for i in range(qtd)]
    return render_to_response("qrcode.html", {'qrcodes': qrcodes})
