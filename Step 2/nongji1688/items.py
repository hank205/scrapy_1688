# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class Nongji1688Item(scrapy.Item):
	nongji_company = Field()
	nongji_url = Field()
	nongji_name = Field()
	nongji_mobilephone = Field()
