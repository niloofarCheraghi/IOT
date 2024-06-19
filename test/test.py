import paho.mqtt.client as mqtt
import time
import random
from pymongo import MongoClient

# Callback called when the client receives a CONNACK message from the broker.
def on_connect(client, userdata, flags, rc):
    print(f"on_connect: Connection result: {mqtt.connack_string(rc)}")
    if rc != 0:
        # If the connection fails, disconnect from the broker
        client.disconnect()

# Callback called when the client knows that a PUBLISH has been successfully sent.
def on_publish(client, userdata, mid):
    print(f"Message with mid {mid} has been published.")

# Function to get temperature data (simulated for demonstration)
def get_temperature():
    time.sleep(1)  # Simulate sensor delay
    return random.randint(0, 100)  # Generate random temperature value

# Function to publish sensor data
def publish_sensor_data(client):
    temperature = get_temperature()
    payload = str(temperature)
    client.publish(topic= "example/temperature", payload=payload, qos=2, retain=False, properties=None)
    # Save data to MongoDB
    save_to_mongodb(temperature)

# Function to save sensor data to MongoDB
def save_to_mongodb(temperature):
    # Connect to MongoDB (replace "mongodb://localhost:27017/" with your MongoDB connection string)
    client = MongoClient("mongodb://f.hadad:038f71df1ab71861a445bad4@mongo-stg-a.alibaba.local:27017,mongo-stg-b.alibaba.local:27017,mongo-stg-c.alibaba.local:27017/acm-core-api?replicaSet=rs0&authSource=admin")
    # Select the database and collection
    db = client["sensor_data"]
    collection = db["temperature"]
    # Insert document
    document = {"temperature": temperature, "timestamp": time.time()}
    collection.insert_one(document)

# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the MQTT broker (replace "test.mosquitto.org" with your broker address)
client.connect("localhost", 1883, 60)

# Start the loop to handle network traffic
client.loop_start()

# Publish sensor data periodically
try:
    while True:
        publish_sensor_data(client)
except KeyboardInterrupt:
    # Disconnect the client and stop the loop on keyboard interrupt
    client.disconnect()
    client.loop_stop()
