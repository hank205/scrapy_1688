# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class Nongji1688Pipeline(object):
	def __init__(self):  
		self.file = codecs.open('nongji1688.json', 'wb', encoding='utf-8')  
		pass

	def process_item(self, item, spider):  
		line = json.dumps(dict(item)) + '\n'  
		#print line

		line = line.replace('[', '')
		line = line.replace(']', '')

		self.file.write(line.decode("unicode_escape")) 
		
		return item