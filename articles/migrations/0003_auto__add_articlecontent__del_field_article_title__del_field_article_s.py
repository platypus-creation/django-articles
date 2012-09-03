# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'ArticleContent'
        db.create_table('articles_articlecontent', (
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'contents', to=orm['articles.Article'])),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(db_index=True, unique=True, max_length=100, populate_from='title', blank=True)),
        ))
        db.send_create_signal('articles', ['ArticleContent'])

        # Deleting field 'Article.title'
        db.delete_column('articles_article', 'title')

        # Deleting field 'Article.slug'
        db.delete_column('articles_article', 'slug')

        # Deleting field 'Article.content'
        db.delete_column('articles_article', 'content')

        # Changing field 'Article.picture'
        db.alter_column('articles_article', 'picture', self.gf('django.db.models.fields.files.ImageField')(max_length=255))
    
    
    def backwards(self, orm):
        
        # Deleting model 'ArticleContent'
        db.delete_table('articles_articlecontent')

        # Adding field 'Article.title'
        db.add_column('articles_article', 'title', self.gf('django.db.models.fields.CharField')(default='title', max_length=255, blank=True), keep_default=False)

        # Adding field 'Article.slug'
        db.add_column('articles_article', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(default='titlt', populate_from='title', max_length=100, blank=True, unique=True, db_index=True), keep_default=False)

        # Adding field 'Article.content'
        db.add_column('articles_article', 'content', self.gf('django.db.models.fields.TextField')(default='content', blank=True), keep_default=False)

        # Changing field 'Article.picture'
        db.alter_column('articles_article', 'picture', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True, blank=True))
    
    
    models = {
        'articles.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'articles'", 'to': "orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'articles.articlecontent': {
            'Meta': {'object_name': 'ArticleContent'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contents'", 'to': "orm['articles.Article']"}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '100', 'populate_from': "'title'", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'articles.linker': {
            'Meta': {'object_name': 'Linker'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'appears_on'", 'to': "orm['articles.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url_pattern': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['articles']
