
#include "sensor_driver.h"
#include "actuator_control.h"

void setup() {
    Serial.begin(9600);
    SensorDriver::init();
    ActuatorControl::init();
}

void loop() {
    float temp = SensorDriver::readTemperature();
    float humidity = SensorDriver::readHumidity();
    Serial.print("Temp: ");
    Serial.print(temp);
    Serial.print("C, Humidity: ");
    Serial.print(humidity);
    Serial.println("%");

    if (temp > 30.0) {
        ActuatorControl::activate();
    } else {
        ActuatorControl::deactivate();
    }
    delay(2000);  // Log every 2 seconds
}
