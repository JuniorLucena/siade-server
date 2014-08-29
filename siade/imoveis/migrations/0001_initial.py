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

        # Adding model 'HistoricalBairro'
        db.create_table(u'imoveis_historicalbairro', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('municipio_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'imoveis', ['HistoricalBairro'])

        # Adding model 'Bairro'
        db.create_table(u'imoveis_bairro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bairros', to=orm['imoveis.Municipio'])),
            ('codigo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'imoveis', ['Bairro'])

        # Adding model 'HistoricalLogradouro'
        db.create_table(u'imoveis_historicallogradouro', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('municipio_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'imoveis', ['HistoricalLogradouro'])

        # Adding model 'Logradouro'
        db.create_table(u'imoveis_logradouro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.Municipio'], null=True, blank=True)),
        ))
        db.send_create_signal(u'imoveis', ['Logradouro'])

        # Adding model 'HistoricalQuadra'
        db.create_table(u'imoveis_historicalquadra', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('bairro_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'imoveis', ['HistoricalQuadra'])

        # Adding model 'Quadra'
        db.create_table(u'imoveis_quadra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bairro', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quadras', to=orm['imoveis.Bairro'])),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'imoveis', ['Quadra'])

        # Adding model 'HistoricalLadoQuadra'
        db.create_table(u'imoveis_historicalladoquadra', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('quadra_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('logradouro_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'imoveis', ['HistoricalLadoQuadra'])

        # Adding model 'LadoQuadra'
        db.create_table(u'imoveis_ladoquadra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('quadra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lados', to=orm['imoveis.Quadra'])),
            ('logradouro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.Logradouro'], null=True)),
        ))
        db.send_create_signal(u'imoveis', ['LadoQuadra'])

        # Adding model 'HistoricalTipoImovel'
        db.create_table(u'imoveis_historicaltipoimovel', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=3)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'imoveis', ['HistoricalTipoImovel'])

        # Adding model 'TipoImovel'
        db.create_table(u'imoveis_tipoimovel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'imoveis', ['TipoImovel'])

        # Adding model 'HistoricalImovel'
        db.create_table(u'imoveis_historicalimovel', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('lado_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('tipo_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('habitantes', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('caes', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gatos', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ordem', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'imoveis', ['HistoricalImovel'])

        # Adding model 'Imovel'
        db.create_table(u'imoveis_imovel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lado', self.gf('django.db.models.fields.related.ForeignKey')(related_name='imoveis', to=orm['imoveis.LadoQuadra'])),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
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

        # Deleting model 'HistoricalBairro'
        db.delete_table(u'imoveis_historicalbairro')

        # Deleting model 'Bairro'
        db.delete_table(u'imoveis_bairro')

        # Deleting model 'HistoricalLogradouro'
        db.delete_table(u'imoveis_historicallogradouro')

        # Deleting model 'Logradouro'
        db.delete_table(u'imoveis_logradouro')

        # Deleting model 'HistoricalQuadra'
        db.delete_table(u'imoveis_historicalquadra')

        # Deleting model 'Quadra'
        db.delete_table(u'imoveis_quadra')

        # Deleting model 'HistoricalLadoQuadra'
        db.delete_table(u'imoveis_historicalladoquadra')

        # Deleting model 'LadoQuadra'
        db.delete_table(u'imoveis_ladoquadra')

        # Deleting model 'HistoricalTipoImovel'
        db.delete_table(u'imoveis_historicaltipoimovel')

        # Deleting model 'TipoImovel'
        db.delete_table(u'imoveis_tipoimovel')

        # Deleting model 'HistoricalImovel'
        db.delete_table(u'imoveis_historicalimovel')

        # Deleting model 'Imovel'
        db.delete_table(u'imoveis_imovel')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'imoveis.bairro': {
            'Meta': {'ordering': "('municipio',)", 'object_name': 'Bairro'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bairros'", 'to': u"orm['imoveis.Municipio']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'imoveis.historicalbairro': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalBairro'},
            'codigo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'municipio_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'imoveis.historicalimovel': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalImovel'},
            'caes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gatos': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'habitantes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'lado_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'tipo_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'imoveis.historicalladoquadra': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalLadoQuadra'},
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'logradouro_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quadra_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'imoveis.historicallogradouro': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalLogradouro'},
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'municipio_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'imoveis.historicalquadra': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalQuadra'},
            'bairro_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'imoveis.historicaltipoimovel': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalTipoImovel'},
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'imoveis.imovel': {
            'Meta': {'ordering': "('numero',)", 'object_name': 'Imovel'},
            'caes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gatos': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'habitantes': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imoveis'", 'to': u"orm['imoveis.LadoQuadra']"}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.TipoImovel']"})
        },
        u'imoveis.ladoquadra': {
            'Meta': {'ordering': "('numero',)", 'object_name': 'LadoQuadra'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logradouro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.Logradouro']", 'null': 'True'}),
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
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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