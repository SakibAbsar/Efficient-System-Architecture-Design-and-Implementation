
#include "sensor_driver.h"
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void SensorDriver::init() {
    dht.begin();
}

float SensorDriver::readTemperature() {
    return dht.readTemperature();
}

float SensorDriver::readHumidity() {
    return dht.readHumidity();
}
