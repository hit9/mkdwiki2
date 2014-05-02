import re
import unidecode


RE_NON_WORD = re.compile(r'\W+')


def slugify(s):
    s = unidecode.unidecode(s).lower()
    return RE_NON_WORD.sub('-', s)
