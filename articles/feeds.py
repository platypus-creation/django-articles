from django.contrib.syndication.views import Feed
from articles.models import ArticleTranslation
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from django.conf import settings                       
import datetime

class ArticleFeed(Feed):
    title = hasattr(settings, 'ARTICLES_RSS_TITLE') and settings.ARTICLES_RSS_TITLE or _("RSS Title")
    description = hasattr(settings, 'ARTICLES_RSS_DESCRIPTION') and settings.ARTICLES_RSS_DESCRIPTION or ""

    # hard coded to prevent circular imports
    link = '/articles/'

    def get_object(self, request, language):
      return ArticleTranslation.objects.filter(published=True, publication_date__lte=datetime.datetime.now(), language=language or get_language()[:2])

    def items(self, obj):
      return obj.order_by('-publication_date')[:10]

    def item_title(self, item):
      return item.title

    def item_description(self, item):
      return item.content
    
    def item_pubdate(self, item):
      return datetime.datetime.combine(item.publication_date, datetime.time())