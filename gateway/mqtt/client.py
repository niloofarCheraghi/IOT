import paho.mqtt.client as mqtt

class MQTTClient:
    def init(url, port, message_callback = None):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        #client.on_connect = MQTTClient.on_connect
        #client.on_publish = MQTTClient.on_publish
        client.on_message = message_callback if message_callback else MQTTClient.on_message
        client.connect(url, port, 60)
        return client

    def on_connect(client, userdata, flags, rc):
        print(f"on_connect: Connection result: {mqtt.connack_string(rc)}")
        if rc != 0:
            client.disconnect()

    def on_publish(client, userdata, mid):
        print(f"Message with mid {mid} has been published.")

    def on_message(client, userdata, msg):
        print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

    def start(client):
        client.loop_start()

    def stop(client):
        client.disconnect()
        client.loop_stop()

    def publish(client, topic, payload, qos=2, retain=False):
        client.publish(topic, payload, qos, retain)

    def Subscribe(client, topic):
        client.subscribe(topic)