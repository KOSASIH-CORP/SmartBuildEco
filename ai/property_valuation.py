import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def initialize_model():
    # Load dataset
    dataset = pd.read_csv("data/datasets/property_data.csv")

    # Train model
    model = RandomForestRegressor()
    model.fit(dataset.drop("price", axis=1), dataset["price"])

    return model
