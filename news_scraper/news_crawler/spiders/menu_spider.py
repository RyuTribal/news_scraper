from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import FormRequest
from ...urls import valid_url, get_domain, get_scheme
from ..items import NewsCrawlerItem

class MenuSpider(CrawlSpider):
  name = 'menu_spider'
  allowed_domains = None
  start_urls = None

  rules = None
  
  def __init__(self, url='', **kwargs):
        domain_url = get_domain(url)
        url_scheme = get_scheme(url)
        self.allowed_domains = [domain_url]
        self.start_urls = [url_scheme + "://" + domain_url]

        self.rules = (Rule(LxmlLinkExtractor(restrict_xpaths=['/html/body/nav'],allow=self.allowed_domains), callback='parse_obj', follow=True),)
        super().__init__(**kwargs)

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