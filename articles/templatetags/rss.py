from django import template
from django.core.urlresolvers import reverse
from django.conf import settings
register = template.Library()


@register.inclusion_tag('articles/rss.html', takes_context=True)
def rss(context, override=None):
  if 'request' in context:
    request = context['request']
    language = settings.LANGUAGES[settings.DEFAULT_LANGUAGE-1][0]
    if hasattr(request, 'LANGUAGE_CODE'):
      language = request.LANGUAGE_CODE
    language = language[:2]
  
    return {
      'url': override and override or request.build_absolute_uri(reverse('rss_feed', args=[language]))
    }
  return {}