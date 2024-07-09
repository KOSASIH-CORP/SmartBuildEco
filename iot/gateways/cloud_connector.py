import requests
from gateway_config import GatewayConfig

class CloudConnector:
    def __init__(self, config):
        self.config = config
        self.api_key = config.get_api_key()
        self.api_url = config.get_api_url()

    def send_data(self, data):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(self.api_url, json=data, headers=headers)
        return response.json()

    def receive_data(self):
        response = requests.get(self.api_url, headers={'Authorization': f'Bearer {self.api_key}'})
        return response.json()

# Example usage:
config = GatewayConfig('config.json')
cloud_connector = CloudConnector(config)
data = {'temperature': 25, 'humidity': 60}
response = cloud_connector.send_data(data)
print(response)
