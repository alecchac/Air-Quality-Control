import random
import time
#Define Constants
CO2_Warning = 1000 #ppm
CO2_High = 2000 #PPM
PM_Warning = 50
PM_High = 100

def get_simulated_sensor_data():
    co2 = int(random.uniform(400,3000))
    Particulate = int(random.uniform(0,200))
    return co2,Particulate

def get_sensor_state(Data_tuple):
    co2 = Data_tuple[0]
    Particulate = Data_tuple[1]
    CO2_state = ''
    PM_state = ''
    #CO2
    if co2 >0 and co2 <CO2_Warning:
        CO2_state = 'NORMAL'
    elif co2>=CO2_Warning and co2<CO2_High:
        CO2_state = 'WARNING'
    elif co2>CO2_High:
        CO2_state = 'HIGH'
    else:
        CO2_state = 'FAULT'
    if Particulate >0 and Particulate <PM_Warning:
        PM_state = 'NORMAL'
    elif Particulate>=PM_Warning and Particulate<PM_High:
        PM_state = 'WARNING'
    elif Particulate>PM_High:
        PM_state = 'HIGH'
    else:
        PM_state = 'FAULT'
    return CO2_state, PM_state

def set_fan_speed(CO2_PM_data,min_fan_speed = 5,max_fan_speed = 100):
    co2 = CO2_PM_data[0]
    PM = CO2_PM_data[1]
    #Define Gain Values of P here 

if __name__ == "__main__":
    while True:
        simulated_fan_data = get_simulated_sensor_data()
        CO2 = simulated_fan_data[0]
        PM = simulated_fan_data[1]
        sensor_state = get_sensor_state(simulated_fan_data)
        print(f'CO2:{CO2}| {sensor_state[0]}\n PM:{PM}| {sensor_state[1]}')
        time.sleep(5)
        