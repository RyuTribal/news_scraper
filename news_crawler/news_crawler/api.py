# -*- coding: utf-8 -*-


__title__ = "news_crawler"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from .crawler.spiders.sitemap_spider import SitemapNewsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from .crawler import crawler_settings as default_settings


def run(url = '', cache = None, blob_storage = None, **kwargs):
    spider_settings = Settings()
    spider_settings.setmodule(default_settings)
    process = CrawlerProcess(settings=spider_settings)

    process.crawl(SitemapNewsSpider, url=url, cache = cache, blob_storage = blob_storage)

    process.start()