from flask import Flask, request, jsonify
from ai.models.climate_resilience import initialize_model

app = Flask(__name__)

# Initialize AI model
model = initialize_model()

@app.route("/resilience", methods=["POST"])
def calculate_resilience():
    # Get climate data from request
    data = request.get_json()

    # Make prediction using AI model
    prediction = model.predict(data)

    # Return predicted climate resilience
    return jsonify({"resilience": prediction})

if __name__ == "__main__":
    app.run(debug=True)
