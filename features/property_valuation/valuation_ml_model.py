import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class ValuationMLModel:
    def __init__(self):
        self.model = RandomForestRegressor()

    def estimate_value(self, property):
        # Load dataset and train model
        dataset = pd.read_csv("property_data.csv")
        self.model.fit(dataset.drop("price", axis=1), dataset["price"])

        # Estimate property value using trained model
        features = pd.DataFrame([property])
        valuation = self.model.predict(features)
          return valuation[0]
