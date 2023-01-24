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

    def __init__(self, url="", cache=None, blob_storage=None, custom_cat=None, custom_loc=custom_loc, depth_limit=0, **kwargs):
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
        self.custom_cat = custom_cat
        self.custom_loc = custom_loc
        self.custom_settings = {
            'DEPTH_LIMIT': depth_limit
        }

        super().__init__(**kwargs)

    def parse_obj(self, response):
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
                yield response.follow(link, callback=self.parse_obj)

    def insert_tag_into_html(self, html, tags=[]):
        soup = Soup(html, "lxml")
        for tag in tags:
            custom_tag = soup.new_tag('meta')
            custom_tag['property'] = tag[0]
            custom_tag['content'] = tag[1]
            soup.head.append(custom_tag)
        return soup.encode("utf8")
