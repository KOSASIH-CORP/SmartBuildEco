import socket
import json

class InternetOfThings:
    def __init__(self, device_id):
        self.device_id = device_id
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_cloud(self, cloud_ip, cloud_port):
        self.socket.connect((cloud_ip, cloud_port))

    def send_data(self, data):
        json_data = json.dumps(data)
        self.socket.send(json_data.encode('utf-8'))

    def receive_data(self):
        data = self.socket.recv(1024)
        return json.loads(data.decode('utf-8'))

    def disconnect_from_cloud(self):
        self.socket.close()

# Example usage:
iot = InternetOfThings('device_123')
iot.connect_to_cloud('192.168.1.100', 8080)
data = {'temperature': 25, 'humidity': 60}
iot.send_data(data)
response = iot.receive_data()
print(response)
iot.disconnect_from_cloud()
