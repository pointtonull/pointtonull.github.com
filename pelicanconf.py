#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from pelican.plugins import gravatar, github_activity

AUTHOR = 'PointToNull'
SITENAME = "pointtonull's buglist"
SITEURL = 'http://pointtonull.github.com/output'
DISQUS_SITENAME = "blog-pointtonull"
THEME = "notmyidea"
THEME = "simple"

TIMEZONE = 'America/Jujuy'
PLUGINS = [gravatar, github_activity]
GITHUB_ACTIVITY_FEED = 'https://github.com/pointtonull.atom'

DEFAULT_LANG = 'es'

# Blogroll
LINKS =  (
          ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          )

# Social widget
SOCIAL = (
          ('You can add links in your config file', '#'),
          ('Another social link', '#'),
         )

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
