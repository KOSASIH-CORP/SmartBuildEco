import os
import time
from gateway_config import GatewayConfig

class DeviceManager:
    def __init__(self, config):
        self.config = config
        self.devices = self.discover_devices()

    def discover_devices(self):
        devices = []
        for file in os.listdir('/sys/bus/i2c/devices/'):
            if file.startswith('i2c-'):
                devices.append(file)
        return devices

    def read_device_data(self, device):
        with open(f'/sys/bus/i2c/devices/{device}/data', 'r') as f:
            return f.read()

    def send_data_to_cloud(self, data):
        # Implement sending data to cloud using MQTT or HTTP
        pass

# Example usage:
config = GatewayConfig('config.json')
device_manager = DeviceManager(config)
for device in device_manager.devices:
    data = device_manager.read_device_data(device)
    device_manager.send_data_to_cloud(data)
