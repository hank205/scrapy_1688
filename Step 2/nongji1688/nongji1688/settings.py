# -*- coding: utf-8 -*-

# Scrapy settings for nongji1688 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'nongji1688'

SPIDER_MODULES = ['nongji1688.spiders']
NEWSPIDER_MODULE = 'nongji1688.spiders'
import random
DOWNLOAD_DELAY = 5 * random.uniform(0.5,1.5)
ITEM_PIPELINES = {  
    'nongji1688.pipelines.Nongji1688Pipeline':300  
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nongji1688 (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False
#COOKIES_DEBUG = True

# log in using the browser first
HEADER = {
	# delete the code below and write the header found in browser, Network
	'''
	"Host": "www.zhihu.com",
	"Connection": "keep-alive",
	"Cache-Control": "max-age=0",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
	"Referer": "http://www.zhihu.com/people/raymond-wang",
	"Accept-Encoding": "gzip,deflate,sdch",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
	'''
}

COOKIES = {
	# delete the code below and write the cookie found in broswer, Network
	'''
	'checkcode':r'"$2a$10$9FVE.1nXJKq/F.nH62OhCevrCqs4skby2bC4IO6VPJITlc7Sh.NZa"',
	'c_c':r'a153f80493f411e3801452540a3121f7',
	'_ga':r'GA1.2.1063404131.1384259893',
	'zata':r'zhihu.com.021715f934634a988abbd3f1f7f31f37.470330',
	'q_c1':r'59c45c60a48d4a5f9a12a52028a9aee7|1400081868000|1400081868000',
	'_xsrf':r'2a7cf7208bf24dbda3f70d953e948135',
	'q_c0':r'"NmE0NzBjZTdmZGI4Yzg3ZWE0NjhkNjkwZGNiZTNiN2F8V2FhRTQ1QklrRjNjNGhMdQ==|1400082425|a801fc83ab07cb92236a75c87de58dcf3fa15cff"',
	'__utma':r'51854390.1063404131.1384259893.1400518549.1400522270.5',
	'__utmb':r'51854390.4.10.1400522270',
	'__utmc':r'51854390',
	'__utmz':r'51854390.1400513283.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/hallson',
	'__utmv':r'51854390.100-1|2=registration_date=20121016=1^3=entry_date=20121016=1'
	'''
}


# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'nongji1688.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# from rotate_useragent import *
DOWNLOADER_MIDDLEWARES = {
	#'nongji1688.middlewares.MyCustomDownloaderMiddleware': 543,
	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
	'nongji1688.rotate_useragent.RotateUserAgentMiddleware' :400
}


# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'nongji1688.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
