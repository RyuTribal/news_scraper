# -*- coding: utf-8 -*-


__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from scrapy.spiders import SitemapSpider
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from ...urls import valid_url, get_domain, get_scheme
from ..items import NewsCrawlerItem
from scrapy import signals
from pydispatch import dispatcher
from ...db import CacheSQL


class SitemapNewsSpider(SitemapSpider):
    name = "sitemap_spider"
    sitemap_urls = None
    allowed_domains = None

    def __init__(self, url="", pg_creds=None, es_creds=None, **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.sitemap_urls = [url_scheme + "://" + domain_url + "/robots.txt"]
        self.allowed_domains = [domain_url]
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.cache_db = CacheSQL(**pg_creds)
        self.es_creds = es_creds

        super().__init__(**kwargs)

    def check_cache(self, links):
        for link in links:
            if self.cache_db.check_url_exists(link.url):
                continue
            yield link

    def parse(self, response):
        if valid_url(response.url):
            item = NewsCrawlerItem()
            item["url"] = response.url
            self.cache_db.add_url(response.url)
            yield item
        else:
            links = self.check_cache(
                LxmlLinkExtractor(allow=self.allowed_domains).extract_links(response)
            )
            for link in links:
                yield response.follow(link, callback=self.parse)

    def spider_closed(self):
        self.cache_db.close_connection()
