# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from ..article import Article
import os
from ..db import ElasticDB
from elasticsearch.exceptions import RequestError
from ..db import CacheSQL

class NewsCrawlerPipeline:
    file = None

    def open_spider(self, spider):
        # self.file = open('articles.jl', 'w+')
        if hasattr(spider, 'es_db'):
            spider.es_db.connect()
        
        if hasattr(spider, 'cache'):
            spider.cache.connect()

    def close_spider(self, spider):
        # self.file.close()
        spider.cache.close_connection()
        pass

    def process_item(self, item, spider):
        url = ItemAdapter(item).get("url")
        article = Article(url)
        article.build()
        article_dict = article.get_dict()
        final_data = (
            json.dumps(
                article_dict, indent=2, ensure_ascii=False, default=serialize_sets
            )
            + "\n"
        )
        # self.file.write(final_data)
        try:
            spider.es_db.add_document(final_data)
        except RequestError:
            if RequestError.error == 'mapper_parsing_exception':
                formatted_date = format_date(final_data['publish_date'])
                final_data['publish_date'] = formatted_date
                spider.es_db.add_document(final_data)
        if hasattr(spider, 'cache'):
            spider.cache.add_url(url)
        return item


def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)
    elif (
        not isinstance(obj, dict)
        and not isinstance(obj, int)
        and not isinstance(obj, str)
        and not isinstance(obj, list)
        and not isinstance(obj, bool)
        and not obj is None
    ):
        return str(obj)

    return obj


def format_date(time):
    date = time
    date_split = date.split('-')
    year = date_split[0]
    month = date_split[1]
    day = date_split[2]

    time_split = date.split(' ')[1].split(':')
    hour = time_split[0]
    minute = time_split[1]
    seconds = time_split[2]

    final_string = year+month+day+'T'+hour+minute+seconds+'.0000'

    return final_string
