import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class DataAnalytics:
    def __init__(self, data):
        self.data = data

    def preprocess_data(self):
        # Implement data preprocessing logic here
        pass

    def train_model(self):
        X = self.data.drop(['target'], axis=1)
        y = self.data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model

    def make_predictions(self, model):
        predictions = model.predict(self.data)
        return predictions

# Example usage:
data = pd.read_csv('data.csv')
analytics = DataAnalytics(data)
analytics.preprocess_data()
model = analytics.train_model()
predictions = analytics.make_predictions(model)
