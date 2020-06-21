from pymongo import MongoClient
from app import app



CONNECTION_STRING = "mongodb+srv://randellCrapy:<password>@junctionx-mnnrf.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.gettingStarted
# user_collection = PyMongo.collection.Collection(db, 'user_collection')