from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

class someSpider(CrawlSpider):
  name = 'crawltest'
  allowed_domains = ['aftonbladet.se', 'rss.aftonbladet.se']
  start_urls = ['https://www.aftonbladet.se/']

  rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)


  def parse_obj(self,response):
    for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
        with open('log.txt', 'a') as f:
            f.write(link.url + "\n")
        