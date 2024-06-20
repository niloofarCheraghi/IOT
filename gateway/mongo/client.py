from pymongo import MongoClient
import time

class MongoRepo:
    def init():
        client = MongoClient()
        return client
        
    def save_temperature(temperature):
        client = MongoClient('127.0.0.1', 27017)
        db = client["sensor_data"]
        collection = db["temperature"]
        document = {"temperature": temperature, "timestamp": time.time()}
        collection.insert_one(document)
