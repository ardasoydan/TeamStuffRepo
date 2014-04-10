# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'teamstuffapp_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teamstuffapp.User'])),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sport', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('club_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'teamstuffapp', ['Team'])

        # Adding model 'TeamEvent'
        db.create_table(u'teamstuffapp_teamevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teamstuffapp.Team'])),
            ('training_session', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('takes_place_in', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'teamstuffapp', ['TeamEvent'])

        # Adding model 'User'
        db.create_table(u'teamstuffapp_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('birth_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user_type', self.gf('django.db.models.fields.CharField')(default='MAN', max_length=3)),
        ))
        db.send_create_signal(u'teamstuffapp', ['User'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'teamstuffapp_team')

        # Deleting model 'TeamEvent'
        db.delete_table(u'teamstuffapp_teamevent')

        # Deleting model 'User'
        db.delete_table(u'teamstuffapp_user')


    models = {
        u'teamstuffapp.team': {
            'Meta': {'object_name': 'Team'},
            'club_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teamstuffapp.User']"})
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
        u'teamstuffapp.user': {
            'Meta': {'object_name': 'User'},
            'birth_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_type': ('django.db.models.fields.CharField', [], {'default': "'MAN'", 'max_length': '3'})
        }
    }

    complete_apps = ['teamstuffapp']