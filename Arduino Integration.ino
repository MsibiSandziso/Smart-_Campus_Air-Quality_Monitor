#include <EloquentTinyML.h>
#include <eloquent_tinyml/tensorflow.h>
#include "model_data.h"

// Model configuration
#define NUMBER_OF_INPUTS 4
#define NUMBER_OF_OUTPUTS 1
#define TENSOR_ARENA_SIZE 8*1024

Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml;

void setup() {
    Serial.begin(115200);
    ml.begin(comfort_model); // Load the model from model_data.h
}

void loop() {
    // 1. Read sensors
    float pm25 = 15.0; 
    float co = 450.0;
    float temp = 25.5;
    float hum = 45.0;

    // 2. Pre-process (Scale) the data using the parameters above
    float input[4] = {
        (pm25 - 2.0) / (999.0 - 2.0),
        (co - 100.0) / (10000.0 - 100.0),
        (temp - (-19.9)) / (41.6 - (-19.9)),
        (hum - 1.7) / (100.0 - 1.7)
    };

    // 3. Run Inference
    float prediction = ml.predict(input);

    // 4. Output Result (0 = Good, 1 = Poor)
    if (prediction > 0.5) {
        Serial.println("Comfort Status: POOR (Trigger Ventilation)");
    } else {
        Serial.println("Comfort Status: GOOD");
    }
    
    delay(5000);
}
