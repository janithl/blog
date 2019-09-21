#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR      = 'Janith'
SITENAME    = "Janith's Blog"
SITEURL     = ''

RELATIVE_URLS   = True
DEFAULT_LANG    = 'en'
TIMEZONE        = 'Asia/Colombo'

THEME           = 'pelican-readable'
USER_LOGO_URL   = SITEURL + '/static/images/avatar.png'

PATH            = 'content'

ARTICLE_URL     = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL        = '{date:%Y}/{date:%m}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS    = '{date:%Y}/{date:%m}/{slug}-{lang}/index.html'

CATEGORY_URL    = 'category/{slug}/'
CATEGORY_SAVE_AS    = 'category/{slug}/index.html'
AUTHOR_URL      = 'author/{slug}/'
AUTHOR_SAVE_AS  = 'author/{slug}/index.html'
TAG_URL         = 'tag/{slug}/'
TAG_SAVE_AS     = 'tag/{slug}/index.html'

TAGS_URL        = 'tags/'
TAGS_SAVE_AS    = 'tags/index.html'

DEFAULT_PAGINATION  = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

EXTRA_PATH_METADATA = {'images/favicon.ico': {'path': 'favicon.ico'}}
DISQUS_SITENAME     = 'janithl'
GITHUB_URL          = 'https://github.com/janithl'
GOOGLE_ANALYTICS    = 'UA-7602960-7'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM           = None
CATEGORY_FEED_ATOM      = None
TRANSLATION_FEED_ATOM   = None
AUTHOR_FEED_ATOM        = None
AUTHOR_FEED_RSS         = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/janithl'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Turn off syntax highlights
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'guess_lang': False, 'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
