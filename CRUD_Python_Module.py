from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # Connection Variables
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Error inserting document:", e)
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method to implement the R in CRUD
    def read(self, query):
        if query is not None:
            try:
                results = self.collection.find(query)
                return list(results)
            except Exception as e:
                print("Error reading documents:", e)
                return []
        else:
            raise Exception("Nothing to search, because query parameter is empty")
            
    # Update method to implement the U in CRUD
    def update(self, query, new_values): # Update method to modify documents matching query
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values}) # Update all matching documents with provided values
                return result.modified_count
            except Exception as e:
                print("Error updating documents:", e)
                return 0
        else:
            raise Exception("Update failed because query or update data is empty")

    # Delete method to implement the D in CRUD
    def delete(self, query): # Delete method to remove documents matching the query
        if query is not None:
            try:
                result = self.collection.delete_many(query) # Delete all documents that match the query
                return result.deleted_count
            except Exception as e:
                print("Error deleting documents:", e)
                return 0
        else:
            raise Exception("Delete failed because query parameter is empty")