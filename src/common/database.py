import pymongo
from src import secrets
import dns


class Database(object):

    URI = f"mongodb+srv://{secrets.USERNAME}:{secrets.PASSWORD}@cluster0.txbjp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['WhtThePhish']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)