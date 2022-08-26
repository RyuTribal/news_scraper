# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib

class NewsCrawlerPipeline:
    file = None

    def open_spider(self, spider):
        spider.logger.info("Using spider: "+spider.name)
        # if hasattr(spider, 'es_db'):
        #     spider.es_db.connect()
        
        # if hasattr(spider, 'cache'):
        #     spider.cache.connect()

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        url = ItemAdapter(item).get("url")
        html_bytes = ItemAdapter(item).get("html")
        name = urllib.parse.quote(url, safe='')+'.html'
        if hasattr(spider, "blob_storage"):
            spider.blob_storage.upload_file(html_bytes, name)
        return item
