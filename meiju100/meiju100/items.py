# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Meiju100Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movname = scrapy.Field()
    movurl = scrapy.Field()
    movstatu = scrapy.Field()
    movstation = scrapy.Field()
    movupdate = scrapy.Field()
