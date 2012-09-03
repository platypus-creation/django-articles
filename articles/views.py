from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from articles.models import ArticleTranslation

def article(request, language, article_slug):
  if request.user.is_staff:
    article_translation = get_object_or_404(ArticleTranslation, language=language, slug=article_slug)
  else:
    article_translation = get_object_or_404(ArticleTranslation, language=language, slug=article_slug, published=True)
  return render_to_response('articles/article.html', locals(), context_instance=RequestContext(request))