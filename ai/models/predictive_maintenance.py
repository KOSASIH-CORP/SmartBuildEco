import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class PredictiveMaintenanceModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)

    def train(self, data):
        X = data.drop(['failure'], axis=1)
        y = data['failure']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

    def predict(self, data):
        return self.model.predict(data)
