# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'teamstuffapp_user')

        # Adding model 'TeamStuffUser'
        db.create_table(u'teamstuffapp_teamstuffuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('user_type', self.gf('django.db.models.fields.CharField')(default='MAN', max_length=3)),
        ))
        db.send_create_signal(u'teamstuffapp', ['TeamStuffUser'])

        # Deleting field 'Team.user'
        db.delete_column(u'teamstuffapp_team', 'user_id')

        # Adding field 'Team.player'
        db.add_column(u'teamstuffapp_team', 'player',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['teamstuffapp.TeamStuffUser']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'teamstuffapp_user', (
            ('user_type', self.gf('django.db.models.fields.CharField')(default='MAN', max_length=3)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=70, null=True)),
        ))
        db.send_create_signal(u'teamstuffapp', ['User'])

        # Deleting model 'TeamStuffUser'
        db.delete_table(u'teamstuffapp_teamstuffuser')

        # Adding field 'Team.user'
        db.add_column(u'teamstuffapp_team', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['teamstuffapp.User']),
                      keep_default=False)

        # Deleting field 'Team.player'
        db.delete_column(u'teamstuffapp_team', 'player_id')


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
        u'teamstuffapp.team': {
            'Meta': {'object_name': 'Team'},
            'club_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teamstuffapp.TeamStuffUser']"}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'teamstuffapp.teamevent': {
            'Meta': {'object_name': 'TeamEvent'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'takes_place_in': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teamstuffapp.Team']"}),
            'training_session': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teamstuffapp.teamstuffuser': {
            'Meta': {'object_name': 'TeamStuffUser'},
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_type': ('django.db.models.fields.CharField', [], {'default': "'MAN'", 'max_length': '3'})
        }
    }

    complete_apps = ['teamstuffapp']