import os
import sys
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from src.features.property_valuation import valuation_api
from src.features.predictive_maintenance import maintenance_api
from src.features.energy_efficiency import efficiency_api
from src.features.climate_resilience import resilience_api
from src.utils.constants import API_VERSION
from src.utils.helpers import get_config

app = Flask(__name__)
api = Api(app)

# Load configuration from environment variables or config file
config = get_config()

# Define API routes
api.add_resource(valuation_api.PropertyValuationAPI, f'/api/{API_VERSION}/property_valuation')
api.add_resource(maintenance_api.PredictiveMaintenanceAPI, f'/api/{API_VERSION}/predictive_maintenance')
api.add_resource(efficiency_api.EnergyEfficiencyAPI, f'/api/{API_VERSION}/energy_efficiency')
api.add_resource(resilience_api.ClimateResilienceAPI, f'/api/{API_VERSION}/climate_resilience')

# Define error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
