from gateway.mqtt.client import MQTTClient
from sensor.sensor import Sensor
from processor.processor import Processor

def main():
    sensor_mqtt_client = MQTTClient.init("localhost", 1883)
    MQTTClient.start(sensor_mqtt_client)
    sensor = Sensor(sensor_mqtt_client)    
    
    processor_mqtt_client = MQTTClient.init("localhost", 1883, Processor.process_message)
    MQTTClient.Subscribe(processor_mqtt_client, "iot/temperature")
    MQTTClient.start(processor_mqtt_client)
    
    try:
        while True:
            sensor.publish_data()
    except KeyboardInterrupt:
        MQTTClient.stop(sensor_mqtt_client)
        MQTTClient.stop(processor_mqtt_client)

if __name__ == "__main__":
    main()
