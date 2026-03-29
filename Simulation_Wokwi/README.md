Circuit Components:

-ESP32 DevKit V1 (30-pin version)

-DHT22 (Connected to Pin D15)

-Potentiometer (Simulating MQ135 Gas Sensor on Pin D34)

Required Libraries:

-DHT sensor library

-EloquentTinyML (for running the neural network)

Testing Procedure
-Adjust Temperature: Click the DHT22 sensor and move the slider above 32°C.

-Adjust Gas Levels: Rotate the Potentiometer dial to simulate high CO concentrations.

-Check Serial Monitor: The system will output a "POOR QUALITY" alert when the AI detects uncomfortable conditions.

The AI Model
The model was trained using a dense neural network to evaluate four features:

-PM2.5

-CO Levels

-Temperature

-Humidity
