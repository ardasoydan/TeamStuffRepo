# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.email'
        db.add_column(u'teamstuffapp_user', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=70, unique=True, null=True),
                      keep_default=False)


        # Changing field 'User.birth_date'
        db.alter_column(u'teamstuffapp_user', 'birth_date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Deleting field 'User.email'
        db.delete_column(u'teamstuffapp_user', 'email')


        # Changing field 'User.birth_date'
        db.alter_column(u'teamstuffapp_user', 'birth_date', self.gf('django.db.models.fields.DateTimeField')())

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
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '70', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_type': ('django.db.models.fields.CharField', [], {'default': "'MAN'", 'max_length': '3'})
        }
    }

    complete_apps = ['teamstuffapp']