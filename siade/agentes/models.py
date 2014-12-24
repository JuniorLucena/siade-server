# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin, Group)
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


class Agente(AbstractBaseUser, PermissionsMixin):
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

    _default_manager = AgenteManager()
    objects = _default_manager
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nome', 'sobrenome']

    def __unicode__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        try:
            group = Group.objects.get(name=self.get_tipo_display())
            self.groups.add(group)
        except:
            pass

        return super(Agente, self).save(*args, **kwargs)

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

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def is_active(self):
        return self.ativo

    class Meta:
        verbose_name = 'agente'
        verbose_name_plural = 'agentes'
