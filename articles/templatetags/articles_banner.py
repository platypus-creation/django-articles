from django import template
register = template.Library()
from articles.models import ArticleTranslation, Linker
from django.db.models import Q
from django.utils.translation import get_language
import datetime

@register.inclusion_tag('articles/articles_banner.html', takes_context=True)
def articles_banner(context, limit=None):
  try:
    linkers = Linker.objects.filter(url_pattern=context['request'].path).filter(Q(end_date__isnull=True) | Q(end_date__gte=datetime.datetime.now()))
    article_translations = ArticleTranslation.objects.filter(
      article__appears_on__in=list(linkers), 
      publication_date__lte=datetime.datetime.now(),
      language=get_language()[:2]
    ).distinct()

    if not context['request'].user.is_staff:
      article_translations = article_translations.filter(published=True)
      
    more = False
    if limit and not context['request'].GET.get('all_articles', 'false') == 'true':
      more = article_translations.count() > limit
      article_translations = article_translations[:limit]
    
    return {'article_translations': article_translations, 'more': more}
  except Exception:
    return {'article_translations': ArticleTranslation.objects.none(), 'more': False}

@register.inclusion_tag('articles/articles_banner.html', takes_context=True)
def all_articles_banner(context, limit=None):
  try:
    article_translations = ArticleTranslation.objects.filter(language=get_language()[:2], publication_date__lte=datetime.datetime.now())

    if context['request'].user.is_staff:
      article_translations = article_translations.filter(published=True)

    if limit:
      article_translations = article_translations[:limit]
    return {'article_translations': article_translations}
  except Exception:
    return {'article_translations': ArticleTranslation.objects.none()}
