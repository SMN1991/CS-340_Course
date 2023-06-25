from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passwd, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = passwd
        HOST = host
        PORT = port
        DB = database
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert!=0:
                print ("Creation!!!")
                return True
            else:
                print("Missing DATA!!!")
                return False  
        elif data is None:
            print("Missing DATA!!!")
        else:
            raise Exception("Nothing to save, data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria)
            #for document in data:
                #print(document)      
        else:
            data = self.database.animals.find({})
            print ("Not found")
        return data

# Create method to implement the U in CRUD.
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
                print ("Document Updated")
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to update, data parameter is empty!")

# Create method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
                print ("Deleted!")
            else:
                result = "No document found!"
            return result
        else:
            raise Exception("Nothing to delete, data parameter is empty!")