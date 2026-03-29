## Smart Campus Environment & Air Quality Monitor

An AIoT project developed using Scrum methodology. This system monitors air quality (PM2.5, CO, Temp, Humidity) and uses a TinyML model running locally on an ESP32 to predict a "Comfort Index."

### Features
- **Edge AI:** Local inference on ESP32 using TensorFlow Lite Micro.
- **IoT Integration:** Real-time data streaming to Arduino IoT Cloud.
- **Data-Driven:** Model trained on Beijing Multisite Air Quality dataset.

### Repository Structure
- `data_processing/`: Python scripts for data cleaning and RH calculation.
- `ml_models/`: Neural network training scripts and exported models.
- `esp32_firmware/`: C++ code for sensor reading and TinyML inference.

###  Hardware Requirements
- ESP32 Development Board
- DHT22 (Temperature & Humidity)
- MQ135 (Air Quality/CO)

### Wokwi Simulation link
https://wokwi.com/projects/459813373716129793
