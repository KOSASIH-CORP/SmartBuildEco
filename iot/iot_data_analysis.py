import pandas as pd
import numpy as np

class IOTDataAnalysis:
    def __init__(self):
        self.data = pd.DataFrame()

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)

    def preprocess_data(self):
        self.data.dropna(inplace=True)
        self.data.fillna(self.data.mean(), inplace=True)

    def analyze_data(self):
        mean = self.data.mean()
        std = self.data.std()
        return mean, std

    def visualize_data(self):
        self.data.plot(kind='bar')
        plt.show()

# Example usage:
iot_da = IOTDataAnalysis()
iot_da.load_data('data.csv')
iot_da.preprocess_data()
mean, std = iot_da.analyze_data()
print(f'Mean: {mean}, Standard Deviation: {std}')
iot_da.visualize_data()
