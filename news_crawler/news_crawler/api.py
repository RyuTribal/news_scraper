# -*- coding: utf-8 -*-


__title__ = "news_crawler"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from .crawler.spiders.sitemap_spider import SitemapNewsSpider
from .crawler.spiders.menu_spider import MenuSpider
from .crawler.spiders.rss_spider import RssNewsSpider
from .crawler.spiders.utils.detectors import get_sitemap, is_rss
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from .crawler import crawler_settings as default_settings


class API():

    def __init__(self):
        spider_settings = Settings()
        spider_settings.setmodule(default_settings)
        self.process = CrawlerProcess(settings=spider_settings)

    def prepare(self, url = '', cache = None, blob_storage = None, custom_category = None, custom_cat = None, **kwargs):
        if is_rss(url):
            self.process.crawl(RssNewsSpider, url=url, cache = cache, blob_storage = blob_storage, custom_cat=custom_cat)
        elif len(get_sitemap(url)) > 0:
            self.process.crawl(SitemapNewsSpider, url=url, cache = cache, blob_storage = blob_storage, custom_cat=custom_cat)
        else:
            self.process.crawl(MenuSpider, url=url, cache = cache, blob_storage = blob_storage, custom_cat=custom_cat)

    def run(self):
        self.process.start()