# -*- coding: utf-8 -*-

# Scrapy settings for csdn_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'csdn_spider'

SPIDER_MODULES = ['csdn_spider.spiders']
NEWSPIDER_MODULE = 'csdn_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'csdn_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cache-Control': 'max-age=0',
    "Connection": "keep-alive",
    "Cookie": "__yadk_uid=IKz3hFywoR3REsyUpvK7SuSxxUus6wnV; OUTFOX_SEARCH_USER_ID_NCOO=1651632960.8302069; UN=qq_36770320; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; smidV2=201807212009048dfe14a3f899722a7e340d68f4bff390005c10a5560aa5b90; ARK_ID=JSe1642303b2c2fe167a6d5bf4a1075a11e164; UM_distinctid=166379396bc41c-0cd2acd56c0344-51422e1f-1fa400-166379396bd5e5; CNZZDATA1259587897=625573485-1538530683-https%253A%252F%252Fwww.google.co.jp%252F%7C1538530683; ADHOC_MEMBERSHIP_CLIENT_ID1.0=744f7192-af31-95c2-5aa7-acdd940ca8eb; uuid_tt_dd=10_28867322940-1540194336591-311346; _ga=GA1.2.786148592.1543453882; _gid=GA1.2.765512116.1543453882; UserName=qq_36770320; UserInfo=f0q6G3jrWBkQgsq6f8TnsB2%2FiID%2FGdWBapANult8cAEGrqQFDRQPRUr%2FlQ7ZnhAMFYizna2cO19O7sN9HkSx5Sph1H2%2F4PHYy5XdDyPfJg0WmvG8mSZywlzweOcUwCPjP7ruDh1R0NSRw3DLa21UYA%3D%3D; UserToken=3bbebee68d6c4778bed10b41770a3802; UserNick=qq_36770320; AU=0D7; BT=1543492351127; tipShow=true; dc_session_id=10_1543567013507.304972; TY_SESSION_ID=0e0d538c-785c-4ee6-83b7-327aa9f52dc0; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1543575305,1543575325,1543575367,1543576889; dc_tos=pj099k; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1543579113",
    # "Host": "blog.csdn.net",
    "Referer": "https://so.csdn.net/so/search/s.do?q=%E5%8C%BA%E5%9D%97%E9%93%BE&t=blog&p=1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'csdn_spider.middlewares.CsdnSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'csdn_spider.middlewares.CsdnSpiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'csdn_spider.pipelines.CsdnSpiderPipeline': 300,
    'csdn_spider.pipelines.ImagesrenamePipeline': 200,
    'csdn_spider.pipelines.CsdnArticlePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# IMAGES_STORE = r''
import conf
IMAGES_STORE = conf.images_dir