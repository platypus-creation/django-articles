from django import template
from BeautifulSoup import BeautifulSoup
from pygments.lexers import get_lexer_by_name
from pygments import highlight
from pygments.formatters import HtmlFormatter

register = template.Library()

# "article_translation.content|beautifully|safe"
@register.filter(name='beautifully')
def beautifully(content):
  soup = BeautifulSoup(content)
  pres = soup.findAll('pre')
  for pre in pres:
    try:
      pre.replaceWith(pygmentify(''.join(map(str, pre.contents)), pre['class']))
    except:
      pass
  return soup.renderContents()

def pygmentify(code, language):
  return highlight(code, get_lexer_by_name(language), HtmlFormatter(noclasses=False, classprefix=u'pygment_', lineseparator='<br/>')).strip("\n")