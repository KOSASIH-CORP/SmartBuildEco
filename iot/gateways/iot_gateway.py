import socket

class IotGateway:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.socket.connect((host, port))

    def send_data(self, data):
        self.socket.send(data.encode())

    def receive_data(self):
        return self.socket.recv(1024).decode()
