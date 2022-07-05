# -*- coding: utf-8 -*-

# Source objects create an object with extracted articles from
# a URL. 

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

import logging
from urllib.parse import urljoin, urlsplit, urlunsplit

from tldextract import tldextract

from . import network
from . import urls
from . import utils
from .article import Article
from .configuration import Configuration
from .extractors import ContentExtractor
from .settings import ANCHOR_DIRECTORY

log = logging.getLogger(__name__)

class Category(object):
    def __init__(self, url):
        self.url = url
        self.htlm = None
        self.doc = None

class Feed(object):
    def __init__(self, url):
        self.url = url
        self.rss = None

NUM_THREADS_PER_SOURCE_WARN_LIMIT = 5

class Source(object):
    """Sources are abstractions of online news vendors like aftonbladet or dn.
    domain     =  'www.dn.se'
    scheme     =  'http'
    categories =  ['http://dn.com/world', 'http://money.dn.com']
    feeds      =  ['http://dn.com/rss.atom', ..]
    articles   =  [<article obj>, <article obj>, ..]
    brand      =  'dn'
    """

    def __init__(self, url, config=None, **kwargs):
        """The config object for this source will be passed into all of this
        source's children articles unless specified otherwise or re-set.
        """
        if(url is None) or ('://' not in url) or (url[:4] != 'http'):
            raise Exception('Input url is haram')
        
        self.config = config or Configuration()
        self.config = utils.extend_config(self.config, kwargs)

        self.extractor = ContentExtractor(self.config)

        self.url = url
        self.url = urls.prepare_url(url)

        self.domain = urls.get_domain(self.url)
        self.scheme = urls.get_scheme(self.url)

        self.categories = []
        self.feeds = []
        self.articles = []

        self.html = ''
        self.doc = None

        self.logo_url = ''
        self.favicon = ''
        self.brand = tldextract.extract(self.url).domain
        self.description = ''

        self.is_parsed = False
        self.is_downloaded = False

        def build(self):
            """Encapsulates download and basic parsing with lxml."""
            self.download()
            self.parse()

            self.set_categories()
            self.download_categories()
            self.parse_categories()

            self.set_feeds()
            self.download_feeds()

            self.generate_articles()
