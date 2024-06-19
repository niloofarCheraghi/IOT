import paho.mqtt.client as mqtt

# Define callback for when a message is received
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Assign the callback functions
client.on_message = on_message

# Connect to the MQTT broker
client.connect("localhost", 1883, 60)

# Subscribe to the topic
client.subscribe("example/temperature")

# Start the loop to process received messages
client.loop_forever()
