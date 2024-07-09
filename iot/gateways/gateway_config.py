import json

class GatewayConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            return json.load(f)

    def get_device_id(self):
        return self.config['device_id']

    def get_api_key(self):
        return self.config['api_key']

    def get_mqtt_broker(self):
        return self.config['mqtt_broker']

    def get_mqtt_port(self):
        return self.config['mqtt_port']

# Example usage:
config = GatewayConfig('config.json')
print(config.get_device_id())
print(config.get_api_key())
print(config.get_mqtt_broker())
print(config.get_mqtt_port())
