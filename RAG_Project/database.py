from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["rag_database"]

collection = db["documents"]