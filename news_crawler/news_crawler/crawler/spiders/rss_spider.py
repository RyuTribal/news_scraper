# -*- coding: utf-8 -*-

"""
Contains the code for the spider that 
crawls through an rss feed
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from scrapy.spiders import XMLFeedSpider
import scrapy
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from .utils.detectors import valid_url, get_domain, get_scheme
from ..items import NewsCrawlerItem
from bs4 import BeautifulSoup as Soup


class RssNewsSpider(XMLFeedSpider):
    name = "rss_spider"
    allowed_domains = None
    itertag = 'item'
    custom_settings= {
        'ROBOTSTXT_OBEY' : False
    }

    def __init__(self, url="", cache=None, blob_storage=None, custom_cat = None, custom_loc = None, **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.start_urls = [url]
        self.cache = cache
        self.blob_storage = blob_storage
        self.custom_cat = custom_cat
        self.custom_loc = custom_loc
        super().__init__(**kwargs)

    def parse_node(self, response, node):
        url = node.xpath('link/text()').get()
        if url is not None:
            yield response.follow(url, callback=self.parse_obj)
    
    def parse_obj(self, response):
        if valid_url(response.url):
            item = NewsCrawlerItem()
            if self.custom_cat or self.custom_loc:
                tags = []
                if self.custom_cat:
                    tags.append(("news_cat", self.custom_cat))
                if self.custom_loc:
                    tags.append(("news_loc", self.custom_loc))
                item['html'] = self.insert_tag_into_html(response.body.decode("utf-8"), tags=tags)
            else:
                item['html'] = response.body
            item["url"] = response.url
            yield item
    
    def insert_tag_into_html(self, html, tags=[]):
        soup = Soup(html, "lxml")
        for tag in tags:
            custom_tag = soup.new_tag('meta')
            custom_tag['property'] = tag[0]
            custom_tag['content'] = tag[1]
            soup.head.append(custom_tag)
        return soup.encode("utf8")
        
