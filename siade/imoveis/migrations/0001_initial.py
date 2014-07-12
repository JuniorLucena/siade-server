# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UF'
        db.create_table(u'imoveis_uf', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'imoveis', ['UF'])

        # Adding model 'Municipio'
        db.create_table(u'imoveis_municipio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uf', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.UF'])),
            ('codigo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'imoveis', ['Municipio'])

        # Adding model 'Bairro'
        db.create_table(u'imoveis_bairro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bairros', to=orm['imoveis.Municipio'])),
            ('codigo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'imoveis', ['Bairro'])

        # Adding model 'Logradouro'
        db.create_table(u'imoveis_logradouro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.Municipio'], null=True, blank=True)),
        ))
        db.send_create_signal(u'imoveis', ['Logradouro'])

        # Adding model 'Quadra'
        db.create_table(u'imoveis_quadra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bairro', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quadras', to=orm['imoveis.Bairro'])),
            ('numero', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'imoveis', ['Quadra'])

        # Adding model 'LadoQuadra'
        db.create_table(u'imoveis_ladoquadra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('quadra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lados', to=orm['imoveis.Quadra'])),
            ('logradouro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.Logradouro'])),
        ))
        db.send_create_signal(u'imoveis', ['LadoQuadra'])

        # Adding model 'TipoImovel'
        db.create_table(u'imoveis_tipoimovel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'imoveis', ['TipoImovel'])

        # Adding model 'Imovel'
        db.create_table(u'imoveis_imovel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lado', self.gf('django.db.models.fields.related.ForeignKey')(related_name='imoveis', to=orm['imoveis.LadoQuadra'])),
            ('numero', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.TipoImovel'])),
            ('habitantes', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('caes', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gatos', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ordem', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal(u'imoveis', ['Imovel'])


    def backwards(self, orm):
        # Deleting model 'UF'
        db.delete_table(u'imoveis_uf')

        # Deleting model 'Municipio'
        db.delete_table(u'imoveis_municipio')

        # Deleting model 'Bairro'
        db.delete_table(u'imoveis_bairro')

        # Deleting model 'Logradouro'
        db.delete_table(u'imoveis_logradouro')

        # Deleting model 'Quadra'
        db.delete_table(u'imoveis_quadra')

        # Deleting model 'LadoQuadra'
        db.delete_table(u'imoveis_ladoquadra')

        # Deleting model 'TipoImovel'
        db.delete_table(u'imoveis_tipoimovel')

        # Deleting model 'Imovel'
        db.delete_table(u'imoveis_imovel')


    models = {
        u'imoveis.bairro': {
            'Meta': {'ordering': "('municipio',)", 'object_name': 'Bairro'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bairros'", 'to': u"orm['imoveis.Municipio']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'imoveis.imovel': {
            'Meta': {'ordering': "('numero',)", 'object_name': 'Imovel'},
            'caes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gatos': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'habitantes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imoveis'", 'to': u"orm['imoveis.LadoQuadra']"}),
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.TipoImovel']"})
        },
        u'imoveis.ladoquadra': {
            'Meta': {'ordering': "('numero',)", 'object_name': 'LadoQuadra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logradouro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.Logradouro']"}),
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quadra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lados'", 'to': u"orm['imoveis.Quadra']"})
        },
        u'imoveis.logradouro': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Logradouro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.Municipio']", 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'imoveis.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uf': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.UF']"})
        },
        u'imoveis.quadra': {
            'Meta': {'ordering': "('bairro', 'numero')", 'object_name': 'Quadra'},
            'bairro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quadras'", 'to': u"orm['imoveis.Bairro']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'imoveis.tipoimovel': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'TipoImovel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'imoveis.uf': {
            'Meta': {'object_name': 'UF'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['imoveis']