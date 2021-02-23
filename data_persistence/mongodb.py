from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, BulkWriteError, OperationFailure


class MongoDB:
    def __init__(self, uri=None):
        """
        Create a class with a given client. Localhost and 27017 port is used by default
        :param uri: URI format example: 'mongodb://localhost:27017/'
        """

        self.client = None
        try:
            if uri:
                self.client = MongoClient(uri)
            else:
                self.client = MongoClient()

        except ConnectionFailure as e:
            print('Error: ', e)

    def insert_many(self, data):
        """
        Insert many documents to a given collection in a given database.
        :param data: dictionary with db, collection and list_dicts keys to insert.
        :return: result of the insert_many
        """
        db = self.client[data['db']]
        collection = db[data['collection']]
        list_dicts = data['list_dict']
        result = None
        try:
            result = collection.insert_many(list_dicts)
            return result
        except BulkWriteError as e:
            print('Error: ', e)
            return result

    def insert(self, data):
        """
        Insert many documents to a given collection in a given database.
        :param data: dictionary with db, collection and list_dicts keys to insert.
        :return: result of the insert_many
        """
        db = self.client[data['db']]
        collection = db[data['collection']]
        doc = data['document']
        result = None
        try:
            result = collection.insert_one(doc)
            return result
        except BulkWriteError as e:
            print('Error: ', e)
            return result

    def get_by_iswc(self, data):
        """
        Get right owners stored in a collection of a given database by iswc
        :param data: dictionary with db, collection and iswc keys.
        :return:
        """
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
