import os
import sys
from ai import property_valuation
from iot import sensor_data
from blockchain import smart_contract

def main():
    # Initialize AI model
    ai_model = property_valuation.initialize_model()

    # Connect to IoT sensors
    sensor_data.connect_sensors()

    # Deploy smart contract
    smart_contract.deploy_contract()

    # Start application
    print("SmartBuildEco application started")

if __name__ == "__main__":
    main()
