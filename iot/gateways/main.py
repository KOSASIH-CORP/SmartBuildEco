from device_manager import DeviceManager
from mqtt_client import MqttClient
from gateway_config import GatewayConfig

def main():
    config = GatewayConfig('config.json')
    device_manager = DeviceManager(config)
    mqtt_client = MqttClient(config)

    while True:
        for device in device_manager.devices:
            data = device_manager.read_device_data(device)
            mqtt_client.publish(f'smartbuildeco/devices/{device}', data)
        time.sleep(10)

if __name__ == '__main__':
    main()
