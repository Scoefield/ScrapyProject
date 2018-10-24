# -*- coding: utf-8 -*-
import scrapy


class MeijuSpider(scrapy.Spider):
    name = "meiju"
    allowed_domains = ["www.meijutt.com"]
    start_urls = ['http://www.meijutt.com/']

    def parse(self, response):
        pass
