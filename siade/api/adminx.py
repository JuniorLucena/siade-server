from django.utils.translation import gettext as _
import xadmin
from provider.oauth2.models import AccessToken, Grant, Client, RefreshToken

class AccessTokenAdmin(object):
    list_display = ('user', 'client', 'token', 'expires', 'scope',)
    raw_id_fields = ('user',)

class GrantAdmin(object):
    list_display = ('user', 'client', 'code', 'expires',)
    raw_id_fields = ('user',)

class ClientAdmin(object):
    list_display = ('url', 'user', 'redirect_uri', 'client_id', 'client_type')
    raw_id_fields = ('user',)

xadmin.site.register(AccessToken, AccessTokenAdmin)
xadmin.site.register(Grant, GrantAdmin)
xadmin.site.register(Client, ClientAdmin)
xadmin.site.register(RefreshToken)
