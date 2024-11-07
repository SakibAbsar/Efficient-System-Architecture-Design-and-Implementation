#include "sensor_driver.h"
#include "actuator_control.h"

void setup() {
    Serial.begin(9600);
    initializeSensors();
    initializeActuators();
}

void loop() {
    float sensorValue = readSensorData();
    controlActuator(sensorValue);
    delay(1000); // Sample rate of 1 second
}
