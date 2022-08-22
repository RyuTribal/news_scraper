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


def run(url = '', cache = None, blob_storage = None, custom_category = None, **kwargs):
    spider_settings = Settings()
    spider_settings.setmodule(default_settings)
    process = CrawlerProcess(settings=spider_settings)
    if is_rss(url):
        process.crawl(RssNewsSpider, url=url, cache = cache, blob_storage = blob_storage)
    elif len(get_sitemap(url)) > 0:
        process.crawl(SitemapNewsSpider, url=url, cache = cache, blob_storage = blob_storage)
    else:
        process.crawl(MenuSpider, url=url, cache = cache, blob_storage = blob_storage)

    process.start()