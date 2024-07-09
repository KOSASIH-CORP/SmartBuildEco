import unittest
from src.features.predictive_maintenance import maintenance_api

class TestPredictiveMaintenanceAPI(unittest.TestCase):
    def test_get_maintenance_schedule(self):
        # Test get maintenance schedule API
        response = maintenance_api.get_maintenance_schedule()
        self.assertIsNotNone(response)

    def test_post_maintenance_request(self):
        # Test post maintenance request API
        response = maintenance_api.post_maintenance_request()
        self.assertIsNotNone(response)
