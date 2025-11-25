# === database.py ===

from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

users = db["users"]
ads_db = db["ads"]
tasks_db = db["tasks"]
referrals_db = db["referrals"]
