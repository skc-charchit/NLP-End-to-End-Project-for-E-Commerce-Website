from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Specify your database name here
db_name = os.getenv("DB_NAME")
db = client[db_name]

# Specify your default collection name here
collection_name = os.getenv("COLLECTION_NAME")
collection = db[collection_name]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")