from gateway.mongo.client import MongoRepo

class Processor:
    def process_message(client, userdata, msg):
        temperature = int(msg.payload.decode())
        print(f"New temperature received: {temperature}")
        print("--------------------------------")
        MongoRepo.save_temperature(temperature)