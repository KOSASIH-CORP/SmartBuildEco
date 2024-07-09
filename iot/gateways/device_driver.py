import os
import time
import threading
from abc import ABC, abstractmethod

class DeviceDriver(ABC):
    def __init__(self, device_path):
        self.device_path = device_path
        self.data_lock = threading.Lock()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        while True:
            data = self.read_data()
            with self.data_lock:
                self.process_data(data)
            time.sleep(1)

    def process_data(self, data):
        # Implement data processing logic here
        pass

class I2CDeviceDriver(DeviceDriver):
    def __init__(self, device_path):
        super().__init__(device_path)
        self.i2c_bus = os.open(device_path, os.O_RDWR)

    def read_data(self):
        data = os.read(self.i2c_bus, 1024)
        return data

    def write_data(self, data):
        os.write(self.i2c_bus, data)

class SPIDeviceDriver(DeviceDriver):
    def __init__(self, device_path):
        super().__init__(device_path)
        self.spi_bus = os.open(device_path, os.O_RDWR)

    def read_data(self):
        data = os.read(self.spi_bus, 1024)
        return data

    def write_data(self, data):
        os.write(self.spi_bus, data)

# Example usage:
i2c_device = I2CDeviceDriver('/dev/i2c-1')
i2c_device.start()

spi_device = SPIDeviceDriver('/dev/spidev0.0')
spi_device.start()
