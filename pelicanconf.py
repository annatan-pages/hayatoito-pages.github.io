#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hayato Ito'
SITENAME = '[Dev] hayato.io'
# SITEURL = ''
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

FEED_ATOM = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_MAX_ITEMS = 8
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FAVICON = 'static/timer/chocolate.ico'

TYPOGFIFY = True

# http://pythonhosted.org/Markdown/extensions/footnotes.html
# MD_EXTENSIONS += ['footnotes']
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'footnotes']

DISPLAY_CATEGORIES_ON_MENU = None
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = False

THEME = './theme'

STATIC_PATHS = ['images', 'static']

STATIC_PATHS += ['extra/CNAME','extra/robots.txt']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/robots.txt': {'path': 'robots.txt'}}

ARTICLE_EXCLUDES = ['pages', 'extra']

import json

JINJA_FILTERS = { 'jsonify': json.dumps,
#                  'mydebug': mydebug
}

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['neighbors', 'sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

DEFAULT_PAGINATION = 8

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

ARCHIVES_SAVE_AS = 'archives/index.html'


# My own settings.
GOOGLE_PLUS_PROFILE_URL = 'https://plus.google.com/+HayatoIto/posts'

ARTICLE_PAGER = True

# Social
GOOGLE_PLUS_BUTTON = True
TWITTER_BUTTON = True
# TWITTER_USERNAME = ''
# TWITTER_HASHTAG = 'hayatoio'
GOOGLE_PLUS_COMMENTS = False
