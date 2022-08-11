# -*- coding: utf-8 -*-

"""
This file contains different middlewares used in
for scrapy.
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

from scrapy.exceptions import IgnoreRequest
import logging

log = logging.getLogger(__name__)


class ByPassUrlMiddleware(object):
    """Skips Parsed Urls."""

    def __init__(self):
        super().__init__()

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

    def process_request(self, request, spider):
        # URL being scraped
        url_exists = spider.cache.check_url_exists(request.url)
        if url_exists:
            raise IgnoreRequest("Skipping URL. Already scrapped or in pipeline.")
        else:
            return None

    def process_exception(self, request, exception, spider):
        spider.logger.info(
            "Skipping Request for url: %s with exception: %s", request.url, exception
        )
        return None
