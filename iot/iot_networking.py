import socket
import threading

class IOTNetworking:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_gateway(self, gateway_ip, gateway_port):
        self.socket.connect((gateway_ip, gateway_port))

    def send_data(self, data):
        self.socket.send(data.encode('utf-8'))

    def receive_data(self):
        data = self.socket.recv(1024)
        return data.decode('utf-8')

    def start_listening(self):
        threading.Thread(target=self.listen_for_data).start()

    def listen_for_data(self):
        while True:
            data = self.receive_data()
            print(f'Received data: {data}')

# Example usage:
iot_net = IOTNetworking()
iot_net.connect_to_gateway('192.168.1.100', 8080)
iot_net.send_data('Hello, IoT gateway!')
iot_net.start_listening()
