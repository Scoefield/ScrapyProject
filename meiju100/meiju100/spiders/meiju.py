# -*- coding: utf-8 -*-
import scrapy
from meiju100.items import Meiju100Item


class MeijuSpider(scrapy.Spider):
    name = "meiju"
    allowed_domains = ["www.meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        for sub in li_list:
            item = Meiju100Item()
            item['movname'] = sub.xpath('./h5/a/text()').extract_first()
            item['movurl'] = response.urljoin(sub.xpath('./h5/a/@href').extract_first())
            item['movstatu'] = sub.xpath('./span[1]/font/text()').extract_first()
            item['movstation'] = sub.xpath('./span[2]/text()').extract_first()
            item['movupdate'] = sub.xpath('./div[2]/text()').extract_first()

            if item['movstatu']:
                pass
            else:
                item['movstatu'] = sub.xpath('./span[1]/text()').extract_first()

            if item['movstation']:
                pass
            else:
                item['movstation'] = [u'未知']
            
            if item['movupdate']:
                pass
            else:
                item['movupdate'] = sub.xpath('./div[2]/font/text()').extract_first()
            yield item
