import unittest
from ai.models.property_valuation import PropertyValuationModel

class TestPropertyValuationModel(unittest.TestCase):
    def test_train(self):
        model = PropertyValuationModel()
        data = pd.read_csv('data.csv')
        model.train(data)
        self.assertIsNotNone(model.model)

    def test_predict(self):
        model = PropertyValuationModel()
        data = pd.read_csv('data.csv')
        prediction = model.predict(data)
        self.assertIsNotNone(prediction)

if __name__ == '__main__':
    unittest.main()
