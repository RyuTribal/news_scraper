# -*- coding: utf-8 -*-

"""
Contains the code for the spider that 
crawls through a sitemap
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from scrapy.spiders import SitemapSpider
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from .utils.detectors import valid_url, get_domain, get_scheme
from ..items import NewsCrawlerItem
from bs4 import BeautifulSoup as Soup


class SitemapNewsSpider(SitemapSpider):
    name = "sitemap_spider"
    sitemap_urls = None
    allowed_domains = None

    def __init__(self, url="", cache=None, blob_storage=None, custom_cat=None, custom_loc=custom_loc, **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.sitemap_urls = [url_scheme + "://" + domain_url + "/robots.txt"]
        self.allowed_domains = [domain_url]
        self.cache = cache
        self.blob_storage = blob_storage
        self.custom_cat = custom_cat
        self.custom_loc = custom_loc
        super().__init__(**kwargs)

    def parse(self, response):
        if valid_url(response.url):
            item = NewsCrawlerItem()
            if self.custom_cat or self.custom_loc:
                tags = []
                if self.custom_cat:
                    tags.append(("news_cat", self.custom_cat))
                if self.custom_loc:
                    tags.append(("news_loc", self.custom_loc))
                item['html'] = self.insert_tag_into_html(
                    response.body.decode("utf-8"), tags=tags)
            else:
                item['html'] = response.body
            item["url"] = response.url
            yield item
        else:
            links = LxmlLinkExtractor(
                allow=self.allowed_domains).extract_links(response)
            for link in links:
                yield response.follow(link, callback=self.parse)

    def insert_tag_into_html(self, html, tags=[]):
        soup = Soup(html, "lxml")
        for tag in tags:
            custom_tag = soup.new_tag('meta')
            custom_tag['property'] = tag[0]
            custom_tag['content'] = tag[1]
            soup.head.append(custom_tag)
        return soup.encode("utf8")
