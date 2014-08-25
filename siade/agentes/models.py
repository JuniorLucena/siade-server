from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords


class AgenteManager(BaseUserManager):
    def create_user(self, codigo, nivel, password=None):
        if not codigo:
            raise ValueError('Agentes devem possuir codigo')

        user = self.model(codigo=codigo, nivel=nivel)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, codigo, password):
        user = self.create_user(codigo, 3, password=password)
        return user


class Agente(AbstractBaseUser):
    '''
    Um agente de endemias
    '''
    nome = models.CharField(max_length=30, verbose_name=_('nome'))
    sobrenome = models.CharField(max_length=30, verbose_name=_('sobrenome'))
    email = models.EmailField(blank=True, verbose_name=_('e-mail'))
    telefone = models.BigIntegerField(blank=True, null=True,
                                      verbose_name=_('telefone'))
    nascimento = models.DateField(blank=True, null=True,
                                  verbose_name=_('data de nasc.'))
    codigo = models.CharField(max_length=20, blank=True, unique=True,
                              verbose_name=_('codigo'))
    nivel = models.PositiveIntegerField(default=1)
    ativo = models.BooleanField(default=True, verbose_name=_('ativo'))

    _default_manager = AgenteManager()
    objects = _default_manager
    USERNAME_FIELD = 'codigo'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.get_short_name()

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return '%s %s' % (self.nome, self.sobrenome)

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_superuser(self):
        return self.nivel == 3

    @property
    def is_active(self):
        return self.ativo

    class Meta:
        verbose_name = _('agente')
        verbose_name_plural = _('agentes')
