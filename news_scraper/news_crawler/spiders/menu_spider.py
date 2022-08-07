# -*- coding: utf-8 -*-


__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import FormRequest
from ...urls import valid_url, get_domain, get_scheme
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

    def __init__(self, url="", cache=None, es_db=None, **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.allowed_domains = [domain_url]
        self.start_urls = [url_scheme + "://" + domain_url]
        self.rules = (
            Rule(
                LxmlLinkExtractor(allow=self.allowed_domains),
                callback="parse_obj",
                follow=False,
                process_links='filter_links'
            ),
        )
        self.cache = cache 
        self.es_db = es_db
        super().__init__(**kwargs)

    def filter_links(self, links):
        # Removes URLs that have already been scraped in previous crawling sessions
        for link in links:
            if self.cache.check_url_exists(link):
                continue
            yield link

    def parse_obj(self, response):
        if valid_url(response.url):
            item = NewsCrawlerItem()
            item["url"] = response.url
            yield item
        else:

            links = self.check_cache(
                LxmlLinkExtractor(allow=self.allowed_domains).extract_links(response)
            )
            for link in links:
                yield response.follow(link, callback=self.parse_obj)
