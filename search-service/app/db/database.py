from pymongo import MongoClient
from dotenv import load_dotenv

import os

load_dotenv()

client = MongoClient(
    os.getenv("MONGO_URL")
)

db = client[os.getenv("MONGO_DB")]

search_collection = db["search_items"]