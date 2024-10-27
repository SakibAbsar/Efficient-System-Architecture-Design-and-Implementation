
#include "actuator_control.h"
#define ACTUATOR_PIN 13

void ActuatorControl::init() {
    pinMode(ACTUATOR_PIN, OUTPUT);
}

void ActuatorControl::activate() {
    digitalWrite(ACTUATOR_PIN, HIGH);
}

void ActuatorControl::deactivate() {
    digitalWrite(ACTUATOR_PIN, LOW);
}
