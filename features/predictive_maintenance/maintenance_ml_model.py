import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class MaintenanceMLModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def predict_maintenance(self, equipment):
        # Load dataset and train model
        dataset = pd.read_csv("maintenance_data.csv")
        self.model.fit(dataset.drop("maintenance_needed", axis=1), dataset["maintenance_needed"])

        # Predict maintenance needs using trained model
        features = pd.DataFrame([equipment])
        prediction = self.model.predict(features)
        return prediction[0]
