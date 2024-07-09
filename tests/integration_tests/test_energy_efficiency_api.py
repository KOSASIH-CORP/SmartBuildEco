import unittest
from src.features.energy_efficiency import efficiency_api

class TestEnergyEfficiencyAPI(unittest.TestCase):
    def test_get_energy_efficiency_data(self):
        # Test get energy efficiency data API
        response = efficiency_api.get_energy_efficiency_data()
        self.assertIsNotNone(response)

    def test_post_energy_efficiency_request(self):
        # Test post energy efficiency request API
        response = efficiency_api.post_energy_efficiency_request()
        self.assertIsNotNone(response)
