# -*- coding: utf-8 -*-
import scrapy
from meiju100.items import Meiju100Item


class MeijuSpider(scrapy.Spider):
    name = "meiju"
    allowed_domains = ["www.meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="top-list fn-clear"]/li')

        for sub in li_list:
            item = Meiju100Item()
            item['movname'] = sub.xpath('./h5/a/text()').extract_first()
            item['movurl'] = sub.xpath('./h5/a/@href').extract_first()
            item['movstatu'] = sub.xpath('./span/font/text()').extract_first()
            item['movstation'] = sub.xpath('./span/font/text()').extract_first()
            item['movupdate'] = sub.xpath('./div/font/text()').extract_first()
            yield item
