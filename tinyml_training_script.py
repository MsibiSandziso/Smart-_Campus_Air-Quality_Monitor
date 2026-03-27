import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('cleaned_air_quality.csv')

df

# 2. Separate Features (X) and Target (y)
X = df[['PM2.5', 'CO', 'TEMP', 'HUMIDITY']]
y = df['Comfort_Index']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the data
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the "Shallow" Neural Network
# We use a small architecture to ensure it fits in the ESP32's SRAM
model = tf.keras.Sequential([
    # input Layer (4 sensors) -> Hidden Layer 1 (8 neurons)
    layers.Dense(8, activation='relu', input_shape=(4,)),

    # hidden Layer 2 (4 neurons)
    layers.Dense(4, activation='relu'),

    # Output Layer (1 neuron) - Sigmoid gives a probability between 0 and 1
    layers.Dense(1, activation='sigmoid')
])

# Compile the Model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Trainning the Model
print("Starting training...")
history = model.fit(
    X_train_scaled,
    y_train,
    epochs=10,
    batch_size=64,       # Process 64 rows at a time
    validation_split=0.2, # Use some data to check for overfitting
    verbose=1
)

loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f"Training Complete!")
print(f"Final Accuracy: {accuracy*100:.2f}%")

# Save the Keras Model (Standard Format)
model.save('comfort_model.h5')

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()
