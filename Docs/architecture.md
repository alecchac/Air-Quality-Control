# System Description for the Air Quality Control System

## System Purpose

1. Measure:
   1. PM( Particulate Matter) 2.5 (um)
   2. PM( Particulate Matter) 10 (um)
   3. CO2 Concentration (PPM)
   4. Temperature
   5. Relative Humidity
2. Control Fan Speeds to reduce PM2.5/10 and CO2
3. Handle bad data / system faults properly

## Hardware

1. CO2 Meter
2. PM Meter
3. Temp/Humidity Meter
4. Duct Fans
5. Fan Speed Power Supply
6. Fan Speed Controller, connected to Ardunio

### Controllers

1. Arduino Uno R3: Handles low level fan control and sensor inputs
2. Raspberry Pi 4: Brains of the system: decision logic, control loops, logging data, ROS/CODESYS integration 

## Inputs

1. PM2.5
2. PM10
3. CO2 PPM
4. Temperature
5. Relative Humidity

## Outputs

1. Outside Air Fan Circuit: PWM --> Fan Rotation --> Outside Air Enters Room
2. Air Filter Fan Circuit: PWM --> Fan Rotation --> Air is pulled through air filters

## States (PLC)

•IDLE: System Powered, but control not active, sensors not logging
•NORMAL: System Powered, Auto Control for fans, Sensors logging, normal sensor readings, in range
•WARNING: Measurements approaching thresholds, possibility of damage
•FAULT: Measurements past threshold, bad sensor readings, fan non operational/no feedback
•SAFE: System Powered off, Fans stopped, and Sensor Measurement stopped

## Basic Logic

1. If CO2 is high, pump in outside air (lower CO2 Concentration)
2. If PM is high, run fans through air filters to mechanically filter air and trap particles in the filter media