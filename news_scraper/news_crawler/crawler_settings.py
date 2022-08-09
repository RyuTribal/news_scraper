# Scrapy settings for news_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://docs.scrapy.org/en/latest/topics/settings.html
#     http://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     http://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "news_crawler"
SPIDER_MODULES = ["news_scraper.news_crawler.spiders"]
NEWSPIDER_MODULE = "news_scraper.news_crawler.spiders"
DEPTH_LIMIT = 4
ITEM_PIPELINES = {
    "news_scraper.news_crawler.pipelines.NewsCrawlerPipeline": 100,
}

# USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'news_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'news_crawler.middlewares.NewsCrawlerSpiderMiddleware': 543,
# }

ROTATED_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'news_scraper.news_crawler.middlewares.ByPassUrlMiddleware': 390,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

USER_AGENTS = [
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.0.0 '
     'Safari/537.36'),

    ('Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'CriOS/103.0.5060.63 '
     'Mobile/15E148 '
     'Safari/604.1'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/102.0.5005.63 '
     'Safari/537.36'),

    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/72.0.3626.121 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.5060.114 '
     'Safari/537.36 '
     'Edg/103.0.1264.62'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) '
     'Gecko/20100101 '
     'Firefox/102.0'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) '
     'Gecko/20100101 '
     'Firefox/102.0'),

    ('Mozilla/5.0 (Linux; Android 9; BDL8051C Build/BDL3552T; wv) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Version/4.0 '
     'Chrome/66.0.3359.158 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Linux; Android 8.1.0; jhs561 Build/GIADA.eng.zc.20200922.153858; wv) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Version/4.0 '
     'Chrome/81.0.4044.138 '
     'Safari/537.36'),

    ('Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/15.5 '
     'Mobile/15E148 '
     'Safari/604.1'),

    ('Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Mobile/15E148'),

    ('Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Mobile/15E148'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/15.5 '
     'Safari/605.1.15'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) '
     'Gecko/20100101 '
     'Firefox/102.0'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/13.1.2 '
     'Safari/605.1.15'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Teams/1.5.00.17656 '
     'Chrome/85.0.4183.121 '
     'Electron/10.4.7 '
     'Safari/537.36'),

    ('Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/15.6 '
     'Mobile/15E148 '
     'Safari/604.1'),

    ('Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/15.4 '
     'Mobile/15E148 '
     'Safari/604.1'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/100.0.4896.127 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/101.0.4951.67 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/101.0.4951.54 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.5060.134 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/86.0.4240.198 '
     'Safari/E7FBAF'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.0.0 '
     'Safari/E7FBAF'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.5060.114 '
     'Safari/537.36'),

    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/44.0.2403.157 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/102.0.0.0 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/85.0.4183.38 '
     'Safari/537.36'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.5060.134 '
     'Safari/537.36 '
     'Edg/103.0.1264.71'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.5060.114 '
     'Safari/537.36 '
     'Edg/103.0.1264.49'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/101.0.4951.64 '
     'Safari/537.36 '
     'Edg/101.0.1210.53'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/15.5 '
     'Safari/605.1.15'),

    ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/79.0.3945.88 '
     'Safari/537.36 '
     'Keeper/1616028983'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.5060.53 '
     'Safari/537.36 '
     'Edg/103.0.1264.37'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) '
     'Gecko/20100101 '
     'Firefox/103.0'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.5060.66 '
     'Safari/537.36 '
     'Edg/103.0.1264.44'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/103.0.5060.134 '
     'Safari/537.36 '
     'Edg/103.0.1264.77'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/102.0.5005.124 '
     'Safari/537.36 '
     'Edg/102.0.1245.44'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/15.4 '
     'Safari/605.1.15'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) '
     'Gecko/20100101 '
     'Firefox/98.0'),

    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; WebView/3.0) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/70.0.3538.102 '
     'Safari/537.36 '
     'Edge/18.19044'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/14.1.2 '
     'Safari/605.1.15'),

    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/15.3 '
     'Safari/605.1.15'),

    ('Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) '
     'AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/14.1.2 '
     'Mobile/15E148 '
     'Safari/604.1')
]

ROTATING_PROXY_LIST = [
    'http://mgnvttpo:i2xitrjku85r@45.192.148.87:6421',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.208:5281',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.180:6770',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.121:6455',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.222:5295',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.179:6513',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.154:6337',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.2:6592',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.43:6226',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.77:6411',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.226:6560',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.197:6380',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.174:6357',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.122:6456',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.83:6417',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.161:6495',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.219:6809',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.77:5150',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.77:6667',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.198:6381',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.58:6392',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.216:6550',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.144:6478',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.131:5204',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.40:6374',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.250:6840',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.109:6443',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.158:6748',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.9:5082',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.146:5219',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.168:6502',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.183:6517',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.163:6346',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.176:6510',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.195:6529',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.97:6687',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.108:5181',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.215:5288',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.228:6562',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.246:5319',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.249:6432',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.12:6346',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.36:6370',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.158:5231',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.128:6462',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.177:6767',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.7:6341',
    'http://mgnvttpo:i2xitrjku85r@195.158.192.165:8742',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.225:6559',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.189:6523',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.111:6294',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.184:6367',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.229:6819',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.253:5326',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.189:6372',
    'http://mgnvttpo:i2xitrjku85r@195.158.192.78:8655',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.229:5302',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.69:5142',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.240:6574',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.28:6618',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.212:5285',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.132:6315',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.247:6581',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.11:6345',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.187:6521',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.94:6277',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.245:5318',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.12:6602',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.12:5085',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.231:5304',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.210:6800',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.7:5080',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.140:6730',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.102:6692',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.167:6501',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.223:5296',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.89:5162',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.87:5160',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.54:6237',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.110:6700',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.138:6321',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.51:6385',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.49:5122',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.5:6339',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.195:5268',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.25:5098',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.89:6679',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.66:5139',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.141:6324',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.192:6375',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.127:6461',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.65:6655',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.100:6283',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.113:6296',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.165:5238',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.84:6418',
    'http://mgnvttpo:i2xitrjku85r@45.192.140.171:6761',
    'http://mgnvttpo:i2xitrjku85r@45.192.143.199:5272',
    'http://mgnvttpo:i2xitrjku85r@45.192.148.165:6499',
    'http://mgnvttpo:i2xitrjku85r@45.192.150.118:6301',
]

# scrapy-user-agents
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
#}

# Enable or disable downloader middlewares
# See http://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'news_crawler.middlewares.NewsCrawlerDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'news_crawler.pipelines.NewsCrawlerPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
