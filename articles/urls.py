from django.conf.urls.defaults import *
from articles.models import ArticleTranslation
from articles.feeds import ArticleFeed
from django.utils.translation import get_language

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index', {'queryset': ArticleTranslation.objects.filter(published=True, language=get_language()[:2]),
                                                              'date_field': 'publication_date', 
                                                              'num_latest':10000,
                                                              'template_name': 'articles/article_archive.html',
                                                              'template_object_name': 'article_translations'}, 'articles'),
    (r'^archives/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', {'queryset': ArticleTranslation.objects.filter(published=True, language=get_language()[:2]).order_by('-publication_date'), 
                                                                                      'date_field': 'publication_date',
                                                                                      'template_name': 'articles/article_archive_year.html',
                                                                                      'make_object_list': True}, 'articles_year'),
    (r'^archives/(?P<year>\d{4})/(?P<month>\d{2})/$', 'django.views.generic.date_based.archive_month', {'queryset': ArticleTranslation.objects.filter(published=True, language=get_language()[:2]).order_by('-publication_date'), 
                                                                                                        'date_field': 'publication_date',
                                                                                                        'template_name': 'articles/article_archive_month.html',
                                                                                                        'month_format':'%m'}, 'articles_month'),

    url(r'^(?P<language>[a-z]{2})/rss/$', ArticleFeed(), name='rss_feed'),

    (r'^(?P<language>[a-z]{2})/(?P<article_slug>[\w_-]+)/$', 'articles.views.article'),
)
