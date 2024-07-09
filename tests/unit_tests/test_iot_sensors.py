import unittest
from src.iot.sensors import TemperatureSensor, HumiditySensor, EnergyMeter, WeatherStation

class TestIOTSensors(unittest.TestCase):
    def test_temperature_sensor(self):
        # Test temperature sensor
        sensor = TemperatureSensor()
        self.assertIsNotNone(sensor)

    def test_humidity_sensor(self):
        # Test humidity sensor
        sensor = HumiditySensor()
        self.assertIsNotNone(sensor)

    def test_energy_meter(self):
        # Test energy meter
        sensor = EnergyMeter()
        self.assertIsNotNone(sensor)

    def test_weather_station(self):
        # Test weather station
        sensor = WeatherStation()
        self.assertIsNotNone(sensor)
