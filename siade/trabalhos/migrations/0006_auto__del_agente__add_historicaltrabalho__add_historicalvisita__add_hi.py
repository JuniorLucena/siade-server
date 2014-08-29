# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Agente'
        db.delete_table(u'trabalhos_agente')

        # Adding model 'HistoricalTrabalho'
        db.create_table(u'trabalhos_historicaltrabalho', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('agente_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('ciclo_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('quadra_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('concluido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'trabalhos', ['HistoricalTrabalho'])

        # Adding model 'HistoricalVisita'
        db.create_table(u'trabalhos_historicalvisita', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('imovel_tratado', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('depositos_tratados', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('depositos_eliminados', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('larvicida', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('qtd_larvicida', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('A1', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('A2', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('B', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('C', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('D1', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('D2', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('E', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('amostra_inicial', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('amostra_final', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('tubitos', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('data', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 28, 0, 0))),
            ('hora', self.gf('django.db.models.fields.TimeField')()),
            ('ciclo_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('agente_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('imovel_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('atividade_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('pendencia', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'trabalhos', ['HistoricalVisita'])

        # Adding model 'HistoricalCiclo'
        db.create_table(u'trabalhos_historicalciclo', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('data_inicio', self.gf('django.db.models.fields.DateField')()),
            ('data_fim', self.gf('django.db.models.fields.DateField')()),
            ('fechado_em', self.gf('django.db.models.fields.DateField')(null=True)),
            ('numero', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ano_base', self.gf('django.db.models.fields.PositiveIntegerField')()),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'trabalhos', ['HistoricalCiclo'])


        # Changing field 'Trabalho.agente'
        db.alter_column(u'trabalhos_trabalho', 'agente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agentes.Agente']))

        # Changing field 'Visita.agente'
        db.alter_column(u'trabalhos_visita', 'agente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agentes.Agente']))

    def backwards(self, orm):
        # Adding model 'Agente'
        db.create_table(u'trabalhos_agente', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('nascimento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('bairro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.Bairro'], null=True, blank=True)),
            ('telefone', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'trabalhos', ['Agente'])

        # Deleting model 'HistoricalTrabalho'
        db.delete_table(u'trabalhos_historicaltrabalho')

        # Deleting model 'HistoricalVisita'
        db.delete_table(u'trabalhos_historicalvisita')

        # Deleting model 'HistoricalCiclo'
        db.delete_table(u'trabalhos_historicalciclo')


        # Changing field 'Trabalho.agente'
        db.alter_column(u'trabalhos_trabalho', 'agente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabalhos.Agente']))

        # Changing field 'Visita.agente'
        db.alter_column(u'trabalhos_visita', 'agente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trabalhos.Agente']))

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
        },
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
        },
        u'trabalhos.atividade': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Atividade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'trabalhos.ciclo': {
            'Meta': {'ordering': "('-ano_base', '-numero')", 'object_name': 'Ciclo'},
            'ano_base': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'data_fim': ('django.db.models.fields.DateField', [], {}),
            'data_inicio': ('django.db.models.fields.DateField', [], {}),
            'fechado_em': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'trabalhos.historicalciclo': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalCiclo'},
            'ano_base': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'data_fim': ('django.db.models.fields.DateField', [], {}),
            'data_inicio': ('django.db.models.fields.DateField', [], {}),
            'fechado_em': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'trabalhos.historicaltrabalho': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalTrabalho'},
            'agente_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'ciclo_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'concluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'quadra_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'trabalhos.historicalvisita': {
            'A1': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'A2': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'D1': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'D2': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'E': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalVisita'},
            'agente_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'amostra_final': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'amostra_inicial': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'atividade_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'ciclo_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 28, 0, 0)'}),
            'depositos_eliminados': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'depositos_tratados': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'hora': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'imovel_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'imovel_tratado': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'larvicida': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pendencia': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'qtd_larvicida': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'tubitos': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'trabalhos.trabalho': {
            'Meta': {'object_name': 'Trabalho'},
            'agente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trabalhos'", 'to': u"orm['agentes.Agente']"}),
            'ciclo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trabalhos'", 'to': u"orm['trabalhos.Ciclo']"}),
            'concluido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quadra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trabalhos'", 'to': u"orm['imoveis.Quadra']"})
        },
        u'trabalhos.visita': {
            'A1': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'A2': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'B': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'C': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'D1': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'D2': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'E': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "('data', 'hora', 'ciclo')", 'object_name': 'Visita'},
            'agente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitas'", 'to': u"orm['agentes.Agente']"}),
            'amostra_final': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'amostra_inicial': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'atividade': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitas'", 'to': u"orm['trabalhos.Atividade']"}),
            'ciclo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitas'", 'to': u"orm['trabalhos.Ciclo']"}),
            'data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 28, 0, 0)'}),
            'depositos_eliminados': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'depositos_tratados': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hora': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitas'", 'to': u"orm['imoveis.Imovel']"}),
            'imovel_tratado': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'larvicida': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pendencia': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'qtd_larvicida': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'tubitos': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['trabalhos']