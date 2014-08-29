# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Agente'
        db.create_table(u'agentes_agente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sobrenome', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('telefone', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('nascimento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20, blank=True)),
            ('nivel', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'agentes', ['Agente'])


    def backwards(self, orm):
        # Deleting model 'Agente'
        db.delete_table(u'agentes_agente')


    models = {
        u'agentes.agente': {
            'Meta': {'object_name': 'Agente'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nascimento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sobrenome': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['agentes']