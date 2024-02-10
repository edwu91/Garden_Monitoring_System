import sensors as sensors
import time
import numpy as np

s1 = sensors.sensors()
time.sleep(4)
while True:
    
    time_start_temp = time.time()
    print(s1.get_temperature(), "C")
    time_stop_temp = time.time()
    delta_time = time_stop_temp - time_start_temp
    print("time to get temp: ", delta_time)
    time_start_pressure = time.time()
    print(s1.get_pressure(), "kPa")
    time_stop_pressure = time.time()
    delta_time = time_stop_pressure - time_start_pressure
    print ("time to get pressure: ", delta_time)
    time_start_hum = time.time()
    print(s1.get_humidity(), "%")
    time_stop_hum = time.time()
    delta_time = time_stop_hum - time_start_hum
    print ("time to get hum: ", delta_time)
    time_start_lux = time.time()
    print(s1.get_lux(), "Lx")
    time_stop_lux = time.time()
    delta_time = time_stop_lux - time_start_lux
    print ("time to get lux : ", delta_time)
    time_start_s1 = time.time()
    print(s1.get_moisture_s1(), "%")
    time_stop_s1 = time.time()
    delta_time = time_stop_s1 - time_start_s1
    print("time to get probe moisture: ", delta_time)
    
    time_start_all = time.time()
    #print(s1.get_all(), "%")
    all_dat = s1.get_all()
    time_stop_all = time.time()
    print(all_dat)
    delta_time = time_stop_all - time_start_all
    print("time to get all: ", delta_time)
    time.sleep(2)
