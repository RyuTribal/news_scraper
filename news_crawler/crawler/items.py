# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy




class NewsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()

    def __repr__(self):
        """only print out url after exiting the Pipeline"""
        return repr({"url": self['url']})
