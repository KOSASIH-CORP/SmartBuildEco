from flask import Flask, request, jsonify
from ai.models.energy_efficiency import initialize_model

app = Flask(__name__)

# Initialize AI model
model = initialize_model()

@app.route("/efficiency", methods=["POST"])
def calculate_efficiency():
    # Get energy consumption data from request
    data = request.get_json()

    # Make prediction using AI model
    prediction = model.predict(data)

    # Return predicted energy efficiency
    return jsonify({"efficiency": prediction})

if __name__ == "__main__":
    app.run(debug=True)
