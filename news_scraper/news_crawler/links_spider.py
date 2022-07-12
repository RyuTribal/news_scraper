from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

class BasicSpider(CrawlSpider):
  name = 'basic'

  rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)


  def parse_obj(self,response):
    for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
        with open('log.txt', 'a') as f:
            f.write(link.url + "\n")
        