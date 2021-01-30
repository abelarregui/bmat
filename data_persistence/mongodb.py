from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, BulkWriteError, OperationFailure


class MongoDB:
    def __init__(self, uri=None):
        # URI format: 'mongodb://localhost:27017/'
        self.client = None
        try:
            if uri:
                self.client = MongoClient(uri)
            else:
                self.client = MongoClient()

        except ConnectionFailure as e:
            print('Error: ', e)

    def insert_many(self, data):
        db = self.client[data['db']]
        collection = db[data['collection']]
        list_dicts = data['list_works_dict']
        try:
            result = collection.insert_many(list_dicts)
            return result
        except BulkWriteError as e:
            print('Error: ', e)
            return None

    def get_by_iswc(self, data):
        db = self.client[data['db']]
        collection = db[data['collection']]
        iswc_list = data['iswc']
        dict_find = {"iswc": {"$in": iswc_list}}
        try:
            if iswc_list:
                documents = collection.find(dict_find, {'iswc': 1, 'right_owners': 1, '_id': 0})
            else:
                documents = collection.find()

            output = [{item: data[item] for item in data if item != '_id'} for data in documents]
            return output
        except OperationFailure as e:
            print('Error: ', e)
            return None
