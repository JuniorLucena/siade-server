from cStringIO import StringIO
from qrcode import make as make_qrcode
from base64 import b64encode
from django import template

register = template.Library()

@register.simple_tag
def qr_from_text_img_inline(text):
    data = StringIO()   
    img = make_qrcode(text)
    img.save(data)
    return "data:image/png;base64,%s" % b64encode(data.getvalue())