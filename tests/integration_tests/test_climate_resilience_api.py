import unittest
from src.features.climate_resilience import resilience_api

class TestClimateResilienceAPI(unittest.TestCase):
    def test_get_climate_resilience_data(self):
        # Test get climate resilience data API
        response = resilience_api.get_climate_resilience_data()
        self.assertIsNotNone(response)

    def test_post_climate_resilience_request(self):
        # Test post climate resilience request API
        response = resilience_api.post_climate_resilience_request()
        self.assertIsNotNone(response)
