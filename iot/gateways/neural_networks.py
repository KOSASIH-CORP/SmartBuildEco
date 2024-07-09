import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

class NeuralNetworks:
    def __init__(self, input_shape, num_classes):
        self.model = Sequential()
        self.model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
        self.model.add(MaxPooling2D((2, 2)))
        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D((2, 2)))
        self.model.add(Conv2D(128, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D((2, 2)))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(num_classes, activation='softmax'))

    def compile_model(self):
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def train_model(self, X_train, y_train, X_test, y_test):
        self.model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    def evaluate_model(self, X_test, y_test):
        loss, accuracy = self.model.evaluate(X_test, y_test)
        return accuracy

    def make_predictions(self, X):
        return self.model.predict(X)

# Example usage:
input_shape = (224, 224, 3)
num_classes = 10
neural_networks = NeuralNetworks(input_shape, num_classes)
neural_networks.compile_model()
X_train, X_test, y_train, y_test =...  # Load dataset
neural_networks.train_model(X_train, y_train, X_test, y_test)
accuracy = neural_networks.evaluate_model(X_test, y_test)
print(f'Model accuracy: {accuracy:.2f}%')
