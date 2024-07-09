# API Documentation for SmartBuildEco

## Introduction

SmartBuildEco provides a set of APIs for interacting with the platform. This documentation outlines the available APIs, their endpoints, and their parameters.

## API Endpoints

### Property Valuation API

* **GET /api/v1/property_valuation**: Retrieve a list of property valuations
* **POST /api/v1/property_valuation**: Create a new property valuation
* **GET /api/v1/property_valuation/:id**: Retrieve a specific property valuation
* **PUT /api/v1/property_valuation/:id**: Update a specific property valuation
* **DELETE /api/v1/property_valuation/:id**: Delete a specific property valuation

### Predictive Maintenance API

* **GET /api/v1/predictive_maintenance**: Retrieve a list of predictive maintenance schedules
* **POST /api/v1/predictive_maintenance**: Create a new predictive maintenance schedule
* **GET /api/v1/predictive_maintenance/:id**: Retrieve a specific predictive maintenance schedule
* **PUT /api/v1/predictive_maintenance/:id**: Update a specific predictive maintenance schedule
* **DELETE /api/v1/predictive_maintenance/:id**: Delete a specific predictive maintenance schedule

### Energy Efficiency API

* **GET /api/v1/energy_efficiency**: Retrieve a list of energy efficiency recommendations
* **POST /api/v1/energy_efficiency**: Create a new energy efficiency recommendation
* **GET /api/v1/energy_efficiency/:id**: Retrieve a specific energy efficiency recommendation
* **PUT /api/v1/energy_efficiency/:id**: Update a specific energy efficiency recommendation
* **DELETE /api/v1/energy_efficiency/:id**: Delete a specific energy efficiency recommendation

### Climate Resilience API

* **GET /api/v1/climate_resilience**: Retrieve a list of climate resilience assessments
* **POST /api/v1/climate_resilience**: Create a new climate resilience assessment
* **GET /api/v1/climate_resilience/:id**: Retrieve a specific climate resilience assessment
* **PUT /api/v1/climate_resilience/:id**: Update a specific climate resilience assessment
* **DELETE /api/v1/climate_resilience/:id**: Delete a specific climate resilience assessment

## API Parameters

* `api_key`: Required API key for authentication
* `data`: JSON payload for API requests

## Response Codes

* 200: Success
* 400: Bad Request
* 401: Unauthorized
* 404: Not Found
* 500: Internal Server Error
