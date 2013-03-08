# coding: utf-8
from django.contrib import admin
from articles.models import Article, ArticleTranslation, Linker
from django.conf import settings
from django import forms

##############################
linkerform = forms.ModelForm
if hasattr(settings, 'ARTICLES_LINKER_VALUES'):
    class MyLinkerForm(forms.ModelForm):
        class Meta:
            widgets = {'url_pattern': forms.Select(choices=map(lambda x: (x,x), settings.ARTICLES_LINKER_VALUES))}
            model = Linker
    linkerform = MyLinkerForm

class LinkerInline(admin.StackedInline):
    form = linkerform
    model = Linker
    extra = 1
    classes = ('collapse-open',)
    allow_add = True

##############################
articletranslationform = forms.ModelForm
if len(settings.LANGUAGES) == 1:
    class SingleLanguageForm(forms.ModelForm):
        class Meta:
            model = ArticleTranslation
            exclude = ('language',)        

    articletranslationform = SingleLanguageForm

jsFiles = [settings.STATIC_URL + 'admin/tinymce/jscripts/tiny_mce/tiny_mce.js', settings.STATIC_URL + 'js/tinymce_setup.js',]
if hasattr(settings, 'ARTICLES_JS_FILES'):
    jsFiles = settings.ARTICLES_JS_FILES
if hasattr(settings, 'ARTICLES_USE_MARKDOWN') and settings.ARTICLES_USE_MARKDOWN:
    jsFiles = []
    

class ArticleTranslationInlines(admin.StackedInline):
    model = ArticleTranslation
    form = articletranslationform
    max_num = len(settings.LANGUAGES)
    classes = ('collapse-open',)
    allow_add = False

    class Media:
        js = jsFiles
    
##############################
articleform = forms.ModelForm
exclude = ('head_code',)
if hasattr(settings, 'ARTICLES_HEAD_CODE') and settings.ARTICLES_HEAD_CODE:
    class ArticleForm(forms.ModelForm):
        class Meta:
            widgets = {'head_code': forms.Textarea(attrs={'class':'noEditor'})}
            model = Article
    
    articleform = ArticleForm
    exclude = ()

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTranslationInlines, LinkerInline]
    list_display = ('title', 'created_at')
    form = articleform
    exclude = exclude
    ordering = ('-created_at',)


admin.site.register(Article, ArticleAdmin)


