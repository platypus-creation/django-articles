import unittest

from articles.templatetags.beautifully import *

class TestBeautifully(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass
    
  def test_beautifully(self):
    text = """<p>Qu'est la technique des "sprites", comment &ccedil;a fonctionne et comment la mettre en oeuvre pour &ccedil;a marche sur tous les navigateurs du march&eacute; m&ecirc;me avec des PNG transparents.</p><h2>Concept</h2><p>La technique des sprites n'est pas r&eacute;cente, en fait elle vient du jeu vid&eacute;o (<a title="D&eacute;finition Wikip&eacute;dia du &quot;spriting&quot; dans le jeu vid&eacute;o" href="http://fr.wikipedia.org/wiki/Sprite_(jeu_vid&eacute;o)">D&eacute;finition Wikip&eacute;dia</a>).<br />Le principe c'est d'inclure plusieurs images correspondants &agrave; un contexte dans un seul fichier pour r&eacute;duire le temps de chargement et le poids des images.</p><p>Je vais utiliser comme exemple l'image ci-dessous, qui repr&eacute;sente les deux &eacute;tats de mon ornithorynque.<br />Il n'y a qu'un seul fichier PNG avec de la transparence et mes deux images.<br /><br /><img src="/media/uploads/platypus-sprite.png" alt="Platypus Sprite" width="300" height="120" /><br /><br />Dans le d&eacute;veloppement Web, cette technique permet d'optimiser le temps de chargement de la page et dans le cas d'un changement d'image au survole de la souris, d'&ecirc;tre s&ucirc;r de la r&eacute;activit&eacute; du premier changement.</p><h2>Technique classique</h2><p>La technique la plus utilis&eacute;e est d'afficher l'image en fond en utilisant la propri&eacute;t&eacute; CSS <code>background-image</code> et de changer la position de l'image gr&acirc;ce &agrave; la propri&eacute;t&eacute; <code>background-position</code>.<br />Cette technique fonctionne bien, sauf avec des PNG transparent sur IE6 (Internet Explorer 6).</p><h3>HTML</h3><pre class="html"><a class="sprite" href="#"></a></pre><h3>CSS</h3><pre class="css">.sprite {background: black;}</pre>"""
    expected = """<p>Qu'est la technique des "sprites", comment &ccedil;a fonctionne et comment la mettre en oeuvre pour &ccedil;a marche sur tous les navigateurs du march&eacute; m&ecirc;me avec des PNG transparents.</p><h2>Concept</h2><p>La technique des sprites n'est pas r&eacute;cente, en fait elle vient du jeu vid&eacute;o (<a title='D&eacute;finition Wikip&eacute;dia du "spriting" dans le jeu vid&eacute;o' href="http://fr.wikipedia.org/wiki/Sprite_(jeu_vid&eacute;o)">D&eacute;finition Wikip&eacute;dia</a>).<br />Le principe c'est d'inclure plusieurs images correspondants &agrave; un contexte dans un seul fichier pour r&eacute;duire le temps de chargement et le poids des images.</p><p>Je vais utiliser comme exemple l'image ci-dessous, qui repr&eacute;sente les deux &eacute;tats de mon ornithorynque.<br />Il n'y a qu'un seul fichier PNG avec de la transparence et mes deux images.<br /><br /><img src="/media/uploads/platypus-sprite.png" alt="Platypus Sprite" width="300" height="120" /><br /><br />Dans le d&eacute;veloppement Web, cette technique permet d'optimiser le temps de chargement de la page et dans le cas d'un changement d'image au survole de la souris, d'&ecirc;tre s&ucirc;r de la r&eacute;activit&eacute; du premier changement.</p><h2>Technique classique</h2><p>La technique la plus utilis&eacute;e est d'afficher l'image en fond en utilisant la propri&eacute;t&eacute; CSS <code>background-image</code> et de changer la position de l'image gr&acirc;ce &agrave; la propri&eacute;t&eacute; <code>background-position</code>.<br />Cette technique fonctionne bien, sauf avec des PNG transparent sur IE6 (Internet Explorer 6).</p><h3>HTML</h3><div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #008000; font-weight: bold">&lt;a</span> <span style="color: #7D9029">class=</span><span style="color: #BA2121">&quot;sprite&quot;</span> <span style="color: #7D9029">href=</span><span style="color: #BA2121">&quot;#&quot;</span><span style="color: #008000; font-weight: bold">&gt;&lt;/a&gt;</span><br/></pre></div><h3>CSS</h3><div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #0000FF; font-weight: bold">.sprite</span> {<span style="color: #008000; font-weight: bold">background</span><span style="color: #666666">:</span> <span style="color: #008000">black</span>;}<br/></pre></div>"""
    self.assertEqual(expected, beautifully(text))
    
  def test_pygmentify(self):
    code = '<a class="sprite" href="#"></a>'
    expected = '<div class="highlight" style="background: #f8f8f8"><pre style="line-height: 125%"><span style="color: #008000; font-weight: bold">&lt;a</span> <span style="color: #7D9029">class=</span><span style="color: #BA2121">&quot;sprite&quot;</span> <span style="color: #7D9029">href=</span><span style="color: #BA2121">&quot;#&quot;</span><span style="color: #008000; font-weight: bold">&gt;&lt;/a&gt;</span><br/></pre></div>'
    self.assertEqual(expected, pygmentify(code, 'html'))
