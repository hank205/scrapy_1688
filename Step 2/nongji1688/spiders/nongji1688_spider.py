from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from nongji1688.items import Nongji1688Item

from nongji1688.settings import *
import json
import time
import random

class Nongji1688Spider(Spider):
	"""docstring for Nongji1688Spider"""
	name = "nongji1688"
  
	start_urls = []  
	with open('urls.json') as f:  
	    for line in f:  
	        start_urls.append(json.loads(line))

	def __init__(self):
		self.headers = HEADER
		self.cookies = COOKIES

	def start_requests(self):
		for i, url in enumerate(self.start_urls):
			rand = random.uniform(0.5,1.5)
			time.sleep(rand)
			#print i, url['nongji_url']
			self.headers['Host'] = url['nongji_url'][7:-21]
			self.headers['Referer'] = url['nongji_url']
			# print 'Host', self.headers['Host']
			# print 'Referer', self.headers['Referer']
			yield FormRequest(url['nongji_url'], meta = {'cookiejar': i}, \
				headers = self.headers, \
				cookies = self.cookies, \
				callback = self.parse)#jump to login page


	def parse(self, response):
		# Step two: crawl details
		sel = Selector(response)
		item = Nongji1688Item()
		rand = random.uniform(0.5,1.5)
		time.sleep(rand)

		item['nongji_url'] = sel.url
		item['nongji_company'] = sel.xpath('//div[@class="company-name"]/text()').extract()

		name = sel.xpath('//div[@class="contact-info"]/dl/dd/a[1]/text()').extract()
		title = sel.xpath('//div[@class="contact-info"]/dl/dd/text()').extract()
		title = title[1][0:3]
		item['nongji_name'] = name[0] + title
		# print item['nongji_url']
		# print item['nongji_company']
		# print item['nongji_name']

		phone_number = sel.xpath('//dl[@class="m-mobilephone"]/dd/text()').extract()
		# print '!!!',phone_number
		# print sel.xpath('//div[@class="contcat-desc"]/dl[2]').extract()
		if phone_number != []:
			phone_number = phone_number[0].split('\n')[-2]
			phone_number = phone_number.replace(' ', '')
			item['nongji_mobilephone'] = phone_number
			yield item









