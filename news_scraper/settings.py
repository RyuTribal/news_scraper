# -*- coding: utf-8 -*-

"""
Unlike configuration.py, this file is meant for static, entire project
encompassing settings, like memoization and caching file directories.
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

import logging
import os
import tempfile

from http.cookiejar import CookieJar as cj

from .version import __version__

log = logging.getLogger(__name__)

PARENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

POPULAR_URLS = os.path.join(
    PARENT_DIRECTORY, 'resources/misc/popular_sources.txt')
USERAGENTS = os.path.join(PARENT_DIRECTORY, 'resources/misc/useragents.txt')

STOPWORDS_DIR = os.path.join(PARENT_DIRECTORY, 'resources/text')

# NLP stopwords are != regular stopwords for now...
NLP_STOPWORDS_EN = os.path.join(
    PARENT_DIRECTORY, 'resources/misc/stopwords-nlp-sv.txt')

DATA_DIRECTORY = '.newspaper_scraper'

TOP_DIRECTORY = os.path.join(tempfile.gettempdir(), DATA_DIRECTORY)

# Error log
LOGFILE = os.path.join(TOP_DIRECTORY, 'newspaper_errors_%s.log' % __version__)
MONITOR_LOGFILE = os.path.join(
    TOP_DIRECTORY, 'newspaper_monitors_%s.log' % __version__)

# Memo directory (same for all concur crawlers)
MEMO_FILE = 'memoized'
MEMO_DIR = os.path.join(TOP_DIRECTORY, MEMO_FILE)

# category and feed cache
CF_CACHE_DIRECTORY = 'feed_category_cache'
ANCHOR_DIRECTORY = os.path.join(TOP_DIRECTORY, CF_CACHE_DIRECTORY)

TRENDING_URL = 'http://www.google.com/trends/hottrends/atom/feed?pn=p1'

for path in (TOP_DIRECTORY, MEMO_DIR, ANCHOR_DIRECTORY):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass