# -*- coding: utf-8 -*-


__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import FormRequest
from ...urls import valid_url, get_domain, get_scheme
from ..items import NewsCrawlerItem
from scrapy import signals
from pydispatch import dispatcher
from ...db import CacheSQL


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

    def __init__(self, url="", **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.allowed_domains = [domain_url]
        self.start_urls = [url_scheme + "://" + domain_url]
        self.rules = (
            Rule(
                LxmlLinkExtractor(allow=self.allowed_domains),
                callback="parse_obj",
                process_links="check_cache",
                follow=False,
            ),
        )
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.cache_db = CacheSQL(
            host="localhost", user="root", password="admin", database="crawler"
        )
        super().__init__(**kwargs)

    def check_cache(self, links):
        for link in links:
            if self.cache_db.check_url_exists(link.url):
                continue
            yield link

    def parse_obj(self, response):
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
                yield response.follow(link, callback=self.parse_obj)

    def spider_closed(self):
        self.cache_db.close_connection()
