#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = "content"

AUTHOR = u'CloudFleet Admiralty'
SITENAME = u"CloudFleet - Captain's log"
SITEURL = 'https://cloudfleet.io/blog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DEFAULT_METADATA = {
    'status': 'draft',
}

STATIC_PATHS = ['img', 'video']

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

THEME = u'cloudfleet-pelican'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
