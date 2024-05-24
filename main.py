import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the model
model = Sequential()

# Add the hidden layer (for example, with 10 neurons and ReLU activation)
model.add(Dense(10, activation='relu', input_shape=(n_features,)))

# Add the output layer (for binary classification, use 1 neuron with sigmoid activation)
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()
