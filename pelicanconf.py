#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hayato Ito'
SITENAME = '[Dev] hayato.io'
SITEURL = ''

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

FEED_ATOM = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_MAX_ITEMS = 8
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FAVICON = 'images/favicon.ico'

TYPOGFIFY = True

# http://pythonhosted.org/Markdown/extensions/footnotes.html
MD_EXTENSIONS += ['footnotes']

DISPLAY_CATEGORIES_ON_MENU = None
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = False

THEME = './theme'

STATIC_PATHS = ['images']

STATIC_PATHS += ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

import json

JINJA_FILTERS = { 'jsonify': json.dumps,
#                  'mydebug': mydebug
}

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['neighbors']

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

GOOGLE_PLUS_PROFILE_URL = 'https://plus.google.com/+HayatoIto/posts'
