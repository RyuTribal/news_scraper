# -*- coding: utf-8 -*-


__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from .api import (build, build_article, fulltext, hot, languages,
                  popular_urls, Configuration as Config)
from .article import Article, ArticleException
from .mthreading import NewsPool
from .source import Source
from .version import __version__

news_pool = NewsPool()


# Default logging handler
import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
logging.getLogger(__name__).addHandler(NullHandler())
