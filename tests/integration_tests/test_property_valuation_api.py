import unittest
from src.features.property_valuation import valuation_api

class TestPropertyValuationAPI(unittest.TestCase):
    def test_get_property_valuation(self):
        # Test get property valuation API
        response = valuation_api.get_property_valuation()
        self.assertIsNotNone(response)

    def test_post_property_valuation(self):
        # Test post property valuation API
        response = valuation_api.post_property_valuation()
        self.assertIsNotNone(response)
