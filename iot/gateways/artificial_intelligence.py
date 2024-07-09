import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ArtificialIntelligence:
    def __init__(self):
        self.data = pd.read_csv('data.csv')

    def preprocess_data(self):
        X = self.data.drop('target', axis=1)
        y = self.data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model

    def evaluate_model(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

    def make_predictions(self, model, X):
        return model.predict(X)

# Example usage:
ai = ArtificialIntelligence()
X_train, X_test, y_train, y_test = ai.preprocess_data()
model = ai.train_model(X_train, y_train)
accuracy = ai.evaluate_model(model, X_test, y_test)
print(f'Model accuracy: {accuracy:.2f}%')
