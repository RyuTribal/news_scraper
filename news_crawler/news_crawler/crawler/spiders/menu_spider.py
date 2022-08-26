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
from bs4 import BeautifulSoup as Soup


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

    def __init__(self, url="", cache=None, blob_storage=None, custom_cat = None, **kwargs):
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
        self.blob_storage = blob_storage
        self.cache.connect()
        self.custom_cat = custom_cat
        super().__init__(**kwargs)

    def parse_obj(self, response):
        if valid_url(response.url):
            item = NewsCrawlerItem()
            if self.custom_cat:
                item['html'] = self.insert_tag_into_html(response.body.decode("utf-8"))
            else:
                item['html'] = response.body
            item["url"] = response.url
            yield item
        else:

            links = LxmlLinkExtractor(allow=self.allowed_domains).extract_links(response)
            
            for link in links:
                yield response.follow(link, callback=self.parse_obj)
    
    def insert_tag_into_html(self, html):
        soup = Soup(html, "lxml")
        custom_tag = soup.new_tag('meta')
        custom_tag['property'] = "news_cat"
        custom_tag['content'] = self.custom_cat
        soup.head.append(custom_tag)
        return soup.encode("utf8")
