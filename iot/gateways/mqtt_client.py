import paho.mqtt.client as mqtt
from gateway_config import GatewayConfig

class MqttClient:
    def __init__(self, config):
        self.config = config
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f'Connected to MQTT broker with result code {rc}')

    def on_message(self, client, userdata, message):
        print(f'Received message on topic {message.topic}: {message.payload}')

    def connect(self):
        self.client.connect(self.config.get_mqtt_broker(), self.config.get_mqtt_port())

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def subscribe(self, topic):
        self.client.subscribe(topic)

# Example usage:
config = GatewayConfig('config.json')
mqtt_client = MqttClient(config)
mqtt_client.connect()
mqtt_client.subscribe('smartbuildeco/devices')
