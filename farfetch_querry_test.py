# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from farfetch.farfetch.settings import CONNECTION_STRING


class Farfetchquerry:

    def __init__(self):
        self.con = pymongo.MongoClient(CONNECTION_STRING)
        db=self.con['piyush']
        self.collection = db['farfetch']


    def process_item(self):
        query={"{}":{"$count":"_id"}}
        item=self.collection.find(query)
        return item

result = Farfetchquerry().process_item()
print(str(result))
# count =0
# for i in result:
#     print(i)
#     count+=1
# print("Total Dopcuments are:"+ str(count))