from pymongo import MongoClient
import time

class MongoClient:
    def __init__(self, connection):
        self.client = MongoClient(connection)
        
    def save_temperature(self, temperature):
        db = self.client["sensor_data"]
        collection = db["temperature"]
        document = {"temperature": temperature, "timestamp": time.time()}
        collection.insert_one(document)
