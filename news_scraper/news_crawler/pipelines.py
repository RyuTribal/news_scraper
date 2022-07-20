# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from ..article import Article
import os


class NewsCrawlerPipeline:
    file = None
    def open_spider(self, spider):
        self.file = open('articles.jl', 'w+')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        url = ItemAdapter(item).get('url')
        article = Article(url)
        article.build()
        article_dict = article.get_dict()
        final_data = json.dumps(
            article_dict, indent=2, ensure_ascii=False, default=serialize_sets) + "\n"
        self.file.write(final_data)

        return item


def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)
    elif not isinstance(obj, dict) and not isinstance(obj, int) and not isinstance(obj, str) and not isinstance(obj, list) and not isinstance(obj, bool) and not obj is None:
        return str(obj)

    return obj
