
#ifndef SENSOR_DRIVER_H
#define SENSOR_DRIVER_H

class SensorDriver {
public:
    static void init();
    static float readTemperature();
    static float readHumidity();
};

#endif
