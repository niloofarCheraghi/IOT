import paho.mqtt.client as mqtt

# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Connect to the MQTT broker
client.connect("localhost", 1883, 60)

# Publish a message to the topic
client.publish("farzane/topic", "Hello from Python")

# Disconnect from the broker
client.disconnect()
