# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from news_scraper import Article

class NewsCrawlerPipeline:
    def open_spider(self, spider):
        self.file = open('articles.jl', 'w')

    def close_spider(self, spider):
        self.file.close()


    def process_item(self, item, spider):
        url = ItemAdapter(item).get('url')
        article = Article(url)
        article.download()
        article.parse()
        article_dict = {
            "title": article.title,
            "url": article.url,
            "authors": article.authors,
            "top_img": article.top_image,
            "description": article.meta_description,
            "meta_data": article.meta_data

        }
        final_data = json.dumps(article_dict, indent=2, ensure_ascii=False) + "\n"
        self.file.write(final_data)

        return item
