import unittest
from src.blockchain.smart_contracts import PropertyValuationContract, PredictiveMaintenanceContract, EnergyEfficiencyContract, ClimateResilienceContract

class TestBlockchainContracts(unittest.TestCase):
    def test_property_valuation_contract(self):
        # Test property valuation contract
        contract = PropertyValuationContract()
        self.assertIsNotNone(contract)

    def test_predictive_maintenance_contract(self):
        # Test predictive maintenance contract
        contract = PredictiveMaintenanceContract()
        self.assertIsNotNone(contract)

    def test_energy_efficiency_contract(self):
        # Test energy efficiency contract
        contract = EnergyEfficiencyContract()
        self.assertIsNotNone(contract)

    def test_climate_resilience_contract(self):
        # Test climate resilience contract
        contract = ClimateResilienceContract()
        self.assertIsNotNone(contract)
