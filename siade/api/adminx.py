from django.utils.translation import gettext as _
import xadmin
from oauth2_provider.models import Grant, AccessToken, RefreshToken, get_application_model

class RawIDAdmin(object):
    raw_id_fields = ('user',)

Application = get_application_model()

xadmin.site.register(Application, RawIDAdmin)
xadmin.site.register(Grant, RawIDAdmin)
xadmin.site.register(AccessToken, RawIDAdmin)
xadmin.site.register(RefreshToken, RawIDAdmin)