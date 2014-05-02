# coding=utf8

from . import charset, extension
from .utils import slugify

import houdini
import misaka

from misaka import HtmlRenderer, SmartyPants
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound


class QHtmlRenderer(HtmlRenderer, SmartyPants):

    def __init__(self, *args, **kwargs):
        super(QHtmlRenderer, self).__init__(*args, **kwargs)
        self.title = None

    def _code_no_lexer(self, text):
        text = text.encode(charset).strip()
        return ('<div class="hightlight" <pre><code>%s</code></pre></div>' %
                houdini.escape_html(text))

    def block_code(self, text, lang):
        if not lang:
            return self._code_no_lexer(text)
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            return self._code_no_lexer(text)

        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)

    def header(self, text, level):
        if self.title is None:
            self.title = text
        return '<h{0} id="{2}"><a href="#{2}">{1}</a></h{0}>'.format(
            level,
            text,
            slugify(text)
        )


class Parser(object):

    def __init__(self):
        renderer = QHtmlRenderer()
        extensions = (
            misaka.EXT_FENCED_CODE |
            misaka.EXT_NO_INTRA_EMPHASIS |
            misaka.EXT_AUTOLINK
        )
        self.renderer = renderer
        self.markdown = misaka.Markdown(self.renderer, extensions=extensions)

    def parse(self, text):
        html = self.markdown.render(text)
        title = self.renderer.title
        self.renderer.title = None
        if not title:
            title = 'Untitled'
        return (title, html)


parser = Parser()
