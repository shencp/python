# -*- coding:utf-8 -*-
from pymongo import MongoClient
client = MongoClient()
db = client.test
my_set = db.set
my_set.insert_one({'name':'申传朋','age':'33'})
