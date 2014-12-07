# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from djchoices import DjangoChoices, ChoiceItem


class AgenteManager(BaseUserManager):
    def create_user(self, cpf, nome, sobrenome, tipo, password=None):
        if not cpf:
            raise ValueError('Agentes devem possuir CPF')

        user = self.model(cpf=cpf, nome=nome, sobrenome=sobrenome, tipo=tipo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, nome, sobrenome, password):
        user = self.create_user(cpf, nome, sobrenome,
                                Agente.Tipo.Administrador,
                                password=password)
        return user


class Agente(AbstractBaseUser):
    '''
    Um agente de endemias
    '''
    class Tipo(DjangoChoices):
        '''Possiveis tipos para uma visita'''
        AgenteCampo = ChoiceItem(1, label='Agente de campo')
        Supervisor = ChoiceItem(2, label='Supervisor')
        Administrador = ChoiceItem(99, label='Administrador')

    cpf = models.BigIntegerField(verbose_name='CPF', unique=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    telefone = models.BigIntegerField(blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True,
                                  verbose_name='data de nasc.')
    codigo = models.CharField(max_length=20, unique=True,
                              verbose_name='código')
    tipo = models.PositiveIntegerField(choices=Tipo.choices,
                                       default=Tipo.AgenteCampo)
    ativo = models.BooleanField(default=True)
    is_staff = True

    _default_manager = AgenteManager()
    objects = _default_manager
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nome', 'sobrenome']

    def __unicode__(self):
        return self.get_full_name()

    @property
    def first_name(self):
        return self.nome

    @property
    def last_name(self):
        return self.sobrenome

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return '%s %s' % (self.nome, self.sobrenome)

    def has_perm(self, perm, obj=None):
        if self.tipo == self.Tipo.Administrador:
            return True
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
        return self.tipo == self.Tipo.Administrador

    @property
    def is_active(self):
        return self.ativo

    class Meta:
        verbose_name = 'agente'
        verbose_name_plural = 'agentes'
