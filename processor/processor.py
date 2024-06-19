from gateway.mongo.client import MongoClient

class Processor:
    def process_message(client, userdata, msg):
        temperature = int(msg.payload.decode())
        print(f"New temperature received: {temperature}")
        print("--------------------------------")
        #MongoClient.save_temperature(temperature)