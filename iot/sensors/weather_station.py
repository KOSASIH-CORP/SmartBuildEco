import requests

class WeatherStation:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_data(self):
        # Make API request to weather station
        response = requests.get(f"https://weather-station-api.com/data?api_key={self.api_key}")

        # Return weather data
        return response.json()
