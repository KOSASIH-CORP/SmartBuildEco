import requests

class TemperatureSensor:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_temperature(self):
        # Make API request to temperature sensor
        response = requests.get(f"https://temperature-sensor-api.com/data?api_key={self.api_key}")

        # Return temperature reading
        return response.json()["temperature"]
