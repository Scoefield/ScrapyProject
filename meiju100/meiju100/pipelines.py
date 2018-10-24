# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem


class Meiju100Pipeline(object):

    def __init__(self, mgo_host, mgo_db, mgo_clction):
        self.mgo_host = mgo_host
        self.mgo_db = mgo_db
        self.mgo_clction = mgo_clction

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mgo_host = crawler.settings.get('MGO_HOST'),
            mgo_db = crawler.settings.get('MGO_DB'),
            mgo_clction = crawler.settings.get('MGO_CLCTION')
            )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.mgo_host)
        self.db = self.client[self.mgo_db]

    def process_item(self, item, spider):
        itemdata = dict(item)
        self.db[self.mgo_clction].insert(itemdata)
        return item

    def close_spider(self, spider):
        self.client.close()
