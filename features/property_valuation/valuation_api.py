from flask import Flask, request, jsonify
from ai.models.property_valuation import initialize_model

app = Flask(__name__)

# Initialize AI model
model = initialize_model()

@app.route("/valuate", methods=["POST"])
def valuate_property():
    # Get property data from request
    data = request.get_json()

    # Make prediction using AI model
    prediction = model.predict(data)

    # Return predicted value
    return jsonify({"value": prediction})

if __name__ == "__main__":
    app.run(debug=True)
