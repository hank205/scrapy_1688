from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from nongji1688.items import Nongji1688Item

class Nongji1688Spider(Spider):
	"""docstring for Nongji1688Spider"""
	name = "nongji1688"
	download_delay = 1
	allowed_domains = ["1688.com"]
	start_urls = [
		"http://www.1688.com/chanpin/-C5A9BBFAC5E4BCFE.html?spm=a261b.2187593.1996074689.2.cPWaDw&beginPage=1/"
	]

	def parse(self, response):
		# Step one: crawl urls
		sel = Selector(response)
		item = Nongji1688Item()

		# count how many url links in the page
		counter = 1
		while sel.xpath('//li[@rank="' + str(counter) + '"]') != []:
			counter += 1
		#print 'counter = ', counter

		# get the urls
		for rank in range(1, counter):
			item['nongji_url'] = sel.xpath('//li[@rank="' + str(rank) + '"]/ul/li[@class="sw-mod-offer-block sw-block-company"]/p[@class="sw-block-textP"]/a/@href').extract()[0] + '/page/contactinfo.htm'
			yield item

		# loop through the other pages 1 ... 1000
		for id in range(2, 4):
		 	id = "http://www.1688.com/chanpin/-C5A9BBFAC5E4BCFE.html?spm=a261b.2187593.1996074689.2.cPWaDw&beginPage=" + str(id)
		 	yield Request(id, callback=self.parse)









