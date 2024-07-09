import random

class HumiditySensor:
    def __init__(self):
        self.humidity = 0

    def read_humidity(self):
        self.humidity = random.uniform(40, 60)
        return self.humidity
