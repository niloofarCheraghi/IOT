from sensor.data_simulator import Simulator

class Sensor:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
    
    def publish_data(self):
        temperature = Simulator.get_temperature()
        payload = str(temperature)
        self.mqtt_client.publish("iot/temperature", payload)
        print(f"New temperature sent: {temperature}")
        
