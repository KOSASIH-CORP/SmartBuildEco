import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def initialize_model():
    # Load dataset
    dataset = pd.read_csv("data/datasets/climate_data.csv")

    # Preprocess data
    X = dataset.drop("climate_resilience", axis=1)
    y = dataset["climate_resilience"]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = Sequential()
    model.add(Dense(64, activation="relu", input_shape=(X.shape[1],)))
    model.add(Dense(32, activation="relu"))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error", optimizer="adam")

    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

    return model
