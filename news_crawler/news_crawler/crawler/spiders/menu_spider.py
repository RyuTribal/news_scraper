# -*- coding: utf-8 -*-

"""
Code contains the default spider, crawling
through links
"""

__title__ = "news_crawler"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from .utils.detectors import valid_url, get_domain, get_scheme
from ..items import NewsCrawlerItem


class MenuSpider(CrawlSpider):
    name = "menu_spider"
    allowed_domains = None
    start_urls = None

    rules = None

    # TODO: Make a rule to make use of these bad paths

    bad_paths = [
        "careers",
        "contact",
        "about",
        "faq",
        "terms",
        "privacy",
        "advert",
        "preferences",
        "feedback",
        "info",
        "browse",
        "howto",
        "account",
        "subscribe",
        "donate",
        "shop",
        "admin",
    ]

    def __init__(self, url="", cache=None, **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.allowed_domains = [domain_url]
        self.start_urls = [url_scheme + "://" + domain_url]
        self.rules = (
            Rule(
                LxmlLinkExtractor(allow=self.allowed_domains),
                callback="parse_obj",
                follow=False,
            ),
        )
        self.cache = cache 
        super().__init__(**kwargs)

    def parse_obj(self, response):
        if valid_url(response.url):
            item = NewsCrawlerItem()
            item["url"] = response.url
            item['html'] = response.body
            yield item
        else:

            links = LxmlLinkExtractor(allow=self.allowed_domains).extract_links(response)
            
            for link in links:
                yield response.follow(link, callback=self.parse_obj)
