import scrapy
from tutorial.items import *
from urlparse import urljoin

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["cnmods.org"]
	start_urls = [
	"http://www.cnmods.org"
	]
	base = 'http://www.cnmods.org'

	def parse(self, response):
		for sel in response.xpath('//div[2]//tr//td[1]//div'):
			item = DmozItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['file_urls'] = [urljoin(self.base, ''.join(sel.xpath('a/@href').extract()))]
			yield item