from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned

class Article(models.Model):
  picture = models.ImageField(_(u'Picture'), upload_to=u'uploads/articles', max_length=255) 
  created_at = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, related_name=u"articles")
  head_code = models.TextField(_(u'Head code'), blank=True)

  def __unicode__(self):
    return self.title()
    
  def title(self, language=None):
    l = language or get_language()[:2]
    try:
      return self.translations.get(language=l).title
    except ArticleTranslation.DoesNotExist, e:
      return ""
    except MultipleObjectsReturned, e:
      return "FIX THIS ARTICLE, IT HAS MULTIPLE TRANSLATIONS FOR THE SAME LANGUAGE"

  def content(self, language=None):
    l = language or get_language()[:2]
    try:
      return self.translations.get(language=l).content
    except ArticleTranslation.DoesNotExist, e:
      return ""
    except MultipleObjectsReturned, e:
      return ""
  
  def get_absolute_url(self, language=None):
    l = language or get_language()[:2]
    try:
      return self.translations.get(language=l).get_absolute_url()
    except ArticleTranslation.DoesNotExist, e:
      return ""
    except MultipleObjectsReturned, e:
      return ""
  
  class Meta:
    verbose_name = _(u'Article')
    verbose_name_plural = _(u'Articles')
    ordering = ('created_at',)
    
    
    
class ArticleTranslation(models.Model):
  """(ArticleTranslation description)"""
  article = models.ForeignKey(Article, related_name=u"translations")
  language = models.CharField(_(u'Language'), choices=settings.LANGUAGES, max_length=10)
  title = models.CharField(_(u'Title'), blank=True, max_length=255)
  slug = AutoSlugField(_(u'Slug'), populate_from='title', unique=True, max_length=100)
  published = models.BooleanField(_('Published'), default=False)
  publication_date = models.DateField(_(u'Publication date'), blank=True, null=True)
  content = models.TextField(_(u'Article'), blank=True)
  
  def __unicode__(self):
    return self.language
  
  @models.permalink 
  def get_absolute_url(self):
    return ('articles.views.article', [self.language, self.slug])
  
  def save(self, *args, **kwargs):
    if not self.language:
      self.language = settings.LANGUAGES[settings.DEFAULT_LANGUAGE][0]
    super(ArticleTranslation, self).save(*args, **kwargs)

  def translations(self):
    return self.article.translations.filter(published=True).exclude(id=self.id)
  
  class Meta:
    verbose_name = _(u'Article Translation')
    verbose_name_plural = _(u'Article Translations')
    ordering = ('-publication_date',)


    

class Linker(models.Model):
  """Associate an article to a url"""
  article = models.ForeignKey(Article, related_name=u"appears_on")
  url_pattern = models.CharField(_(u'URL pattern'), max_length=255, help_text=_(u'Path to your page, e.g. /myapp/mypage/'))  
  end_date = models.DateField(_(u'End Date'), blank=True, null=True)

  def __unicode__(self):
    return self.url_pattern

  def clear_cache(self):
    from django.core.cache import cache
    # delete todays cache for active skin to activate new skin
    cache.delete(get_cache_key())

  def save(self, *args, **kwargs):
    self.clear_cache()
    super(Linker, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    self.clear_cache()
    super(Linker, self).delete(*args, **kwargs)


def get_cache_key():
  import datetime
  return 'activeArticleLinkers-' + str(datetime.date.today()) 
