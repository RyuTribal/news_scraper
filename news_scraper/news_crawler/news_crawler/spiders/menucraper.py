from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import FormRequest
from news_scraper.urls import valid_url
from ..items import NewsCrawlerItem

class someSpider(CrawlSpider):
  name = 'Menuscraper'
  allowed_domains = ['www.allehanda.se', 'rss.aftonbladet.se']
  start_urls = ['https://www.allehanda.se/']

  rules = (Rule(LxmlLinkExtractor(restrict_xpaths=['/html/body/nav'],allow=allowed_domains), callback='parse_obj', follow=True),)
    

  def parse_obj(self,response):
    if valid_url(response.url):
      item = NewsCrawlerItem()
      item['url'] = response.url
      yield item
    else: 
      for link in LxmlLinkExtractor(allow=self.allowed_domains).extract_links(response):
        yield response.follow(link, callback=self.parse_obj)

  #  def parse(self, response):
  #       if valid_url(response.url):
  #           item = NewsCrawlerItem()
  #           item['url'] = response.url
  #           yield item

  #  with open('log.txt', 'a') as f:
  #       f.write(response.url + "\n")
  #   yield response.follow(response, callback=self.parse_obj)