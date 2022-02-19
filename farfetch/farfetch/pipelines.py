# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from .settings import CONNECTION_STRING


class FarfetchPipeline(object):

    def __init__(self):
        self.con = pymongo.MongoClient(CONNECTION_STRING)
        db=self.con['piyush']
        self.collection = db['farfetch']


    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
