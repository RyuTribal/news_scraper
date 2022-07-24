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


class NewsCrawlerPipeline:
    file = None

    def open_spider(self, spider):
        # self.file = open('articles.jl', 'w+')
        if 'username' in spider.es_creds and 'password' in spider.es_creds:
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

    def close_spider(self, spider):
        # self.file.close()
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
        self.elastic.add_document(final_data)
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
