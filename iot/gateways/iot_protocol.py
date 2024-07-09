import socket
import json

class IOTProtocol:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send_data(self, data):
        data = json.dumps(data)
        self.socket.sendall(data.encode('utf-8'))

    def receive_data(self):
        data = self.socket.recv(1024)
        data = json.loads(data.decode('utf-8'))
        return data

    def close(self):
        self.socket.close()

# Example usage:
iot_protocol = IOTProtocol('localhost', 8080)
iot_protocol.connect()
data = {'temperature': 25, 'humidity': 60}
iot_protocol.send_data(data)
response = iot_protocol.receive_data()
print(response)
iot_protocol.close()
