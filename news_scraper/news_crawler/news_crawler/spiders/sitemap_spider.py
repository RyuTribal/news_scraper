# -*- coding: utf-8 -*-


__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from scrapy.spiders import SitemapSpider
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from news_scraper.urls import valid_url
from ..items import NewsCrawlerItem


class SitemapNewsSpider(SitemapSpider):
    name = 'sitemap_spider'
    sitemap_urls =  None

    def __init__(self, url='', **kwargs):
        self.sitemap_urls = [url + '/robots.txt']

        super().__init__(**kwargs)

    def parse(self, response):
        if valid_url(response.url):
            item = NewsCrawlerItem()
            item['url'] = response.url
            yield item
