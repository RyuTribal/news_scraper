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
        if hasattr(spider, 'es_creds') and 'username' in spider.es_creds and 'password' in spider.es_creds:
            self.elastic = ElasticDB(
                username=spider.es_creds['username'],
                password=spider.es_creds['password'],
                scheme=spider.es_creds['scheme'],
                host=spider.es_creds['host'],
                port=spider.es_creds['port'],
                index="news_articles",
            )
        else:
            self.elastic = ElasticDB(
                cloud_id = spider.es_creds['host'],
                api_key = spider.es_creds['api_key']
            )
        
        if hasattr(spider, 'cache_creds'):
            self.cache_db = CacheSQL(**spider.cache_creds)

    def close_spider(self, spider):
        # self.file.close()
        self.cache_db.close_connection()
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
            self.elastic.add_document(final_data)
        except RequestError:
            if RequestError.error == 'mapper_parsing_exception':
                formatted_date = format_date(final_data['publish_date'])
                final_data['publish_date'] = formatted_date
                self.elastic.add_document(final_data)
        if hasattr(self, 'cache_db'):
            self.cache_db.add_url(url)
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
