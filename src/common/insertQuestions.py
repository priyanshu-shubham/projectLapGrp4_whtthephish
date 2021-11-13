import uuid

import pymongo

from src.secrets import USERNAME,PASSWORD

class Database(object):

    URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.txbjp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI,connect=False)
        Database.DATABASE = client['WhtThePhish']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)
        
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)
    
Database.initialize()
cur=Database.find('questions',{'category':1})