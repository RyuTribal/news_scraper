# -*- coding: utf-8 -*-


__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from scrapy.spiders import SitemapSpider
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from ...urls import valid_url, get_domain, get_scheme
from ..items import NewsCrawlerItem


class SitemapNewsSpider(SitemapSpider):
    name = "sitemap_spider"
    sitemap_urls = None
    allowed_domains = None

    def __init__(self, url="", cache=None, es_db=None, **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.sitemap_urls = [url_scheme + "://" + domain_url + "/robots.txt"]
        self.allowed_domains = [domain_url]
        self.cache = cache 
        self.es_db = es_db

        super().__init__(**kwargs)

    def parse(self, response):
        if valid_url(response.url):
            item = NewsCrawlerItem()
            item["url"] = response.url
            yield item
        else:
            links = LxmlLinkExtractor(allow=self.allowed_domains).extract_links(response)
            for link in links:
                yield response.follow(link, callback=self.parse)
