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


class RssNewsSpider(XMLFeedSpider):
    name = "rss_spider"
    allowed_domains = None
    itertag = 'item'
    custom_settings= {
        'ROBOTSTXT_OBEY' : False
    }

    def __init__(self, url="", cache=None, blob_storage=None, **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.start_urls = [url]
        self.cache = cache
        self.blob_storage = blob_storage
        self.cache.connect()
        super().__init__(**kwargs)

    def parse_node(self, response, node):
        url = node.xpath('link/text()').get()
        if url is not None:
            yield response.follow(url, callback=self.parse_obj)
    
    def parse_obj(self, response):
        if valid_url(response.url):
            self.logger.info("Found url: "+response.url)
            item = NewsCrawlerItem()
            item["url"] = response.url
            item['html'] = response.body
            yield item
        
