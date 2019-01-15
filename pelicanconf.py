#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pointtonull'
SITENAME = 'Snippets'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Resume (PDF)',
          'https://github.com/pointtonull/cvs/blob/master/CV_Carlos_Cabrera_de_long.pdf'
         ),
         ('Python.org', 'http://python.org/'),
        )

# Social widget
SOCIAL = (
          ("linkedin", "https://www.linkedin.com/in/pointtonull"),
          ("github", "http://github.com/pointtotnull")
         )

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
