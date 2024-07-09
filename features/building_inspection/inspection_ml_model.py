import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class InspectionMLModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def inspect_building(self, building):
        # Load dataset and train model
        dataset = pd.read_csv("building_inspection_data.csv")
        self.model.fit(dataset.drop("inspection_result", axis=1), dataset["inspection_result"])

        # Inspect building using trained model
        features = pd.DataFrame([building])
        inspection = self.model.predict(features)
        return inspection[0]
