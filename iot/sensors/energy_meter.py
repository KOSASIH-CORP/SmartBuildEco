import requests

class EnergyMeter:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_energy_consumption(self):
        # Make API request to energy meter
        response = requests.get(f"https://energy-meter-api.com/data?api_key={self.api_key}")

        # Return energy consumption reading
        return response.json()["energy_consumption"]
