#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL         = 'https://janithl.github.io'
RELATIVE_URLS   = False

FEED_ALL_ATOM           = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM      = 'feeds/%s.atom.xml'
FEED_MAX_ITEMS          = 25

MONTH_ARCHIVE_SAVE_AS   = '{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS    = '{date:%Y}/index.html'

DISPLAY_CATEGORIES_ON_MENU  = True
DISPLAY_TAGS_ON_MENU        = True
