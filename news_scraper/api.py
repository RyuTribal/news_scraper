# -*- coding: utf-8 -*-


__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

import feedparser

from .article import Article
from .configuration import Configuration
from .settings import POPULAR_URLS, TRENDING_URL
from .source import Source
from .utils import extend_config, print_available_languages

def build(url='', dry=False, config=None, **kwargs) -> Source:
    # Returns source object without downloading or parsing
    # the articles
    config = config or Configuration()
    config = extend_config(config, kwargs)
    url = url or ''
    s = Source(url, config=config)
    if not dry:
        s.build()
    return s