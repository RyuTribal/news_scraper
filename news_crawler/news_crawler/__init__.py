# -*- coding: utf-8 -*-


__title__ = "news_crawler"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from .crawler.spiders.utils.db import CacheSQL, CloudBlobStorage
from .api import API

# Default logging handler
import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
logging.getLogger(__name__).addHandler(NullHandler())