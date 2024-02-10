import numpy as np
from datetime import datetime

class Greenhouse_Data_Class:
    #This class is used to store all data belonging to one Bed.
    #this is all the data needed to describe what is monitored from the plant

    def __init__ (self):
        exists = 0
        try:
            self._num_samples = 0
            self._measure_times = []
            self._water_qty = []
            self._temp = []
            self._ambient_light_level = []
            self._humidity = []
            self._pressure = []
        except:
            print("error parsing DataBaseID.txt when initializing class")


    def append_value(self, time, water_qty, temp, light_level, humidity, pressure):
        self._num_samples = self._num_samples + 1
        self._measure_times = np.append(self._measure_times , time)
        self._water_qty = np.append(self._water_qty, water_qty)
        self._temp = np.append(self._temp, temp)
        self._ambient_light_level = np.append(self._ambient_light_level, light_level)
        self._humidity = np.append(self._humidity, humidity)
        self._pressure = np.append(self._pressure, pressure)
        
    def get_values_by_timestamp(self, n):
        return [self._water_qty[n], self._temp[n], self._ambient_light_level[n], self._humidity[n]];

    def set_measure_times(self, n, time):
        if n is not None:
            try:
                self._measure_times[n] = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
            except:
                print("The value is out of range to select measured time")
        else:
            try:
                self._measure_times = time
            except:
                print("too lazy to write an error message")
                
    def init_measure_times(self, time_array):
        try:
            #print("GH init time")
            #print(datetime.strptime(time_array[0], "%Y-%m-%d %H:%M:%S"))
            self._measure_times = [datetime.strptime(s, "%Y-%m-%d %H:%M:%S") for s in time_array]
        except:
            print("could not init measured time array")
    def append_measure_times(self, time_array, time):
        return 1
        
    def get_measure_times(self,n=None):
        if n is not None:
            try:
                return self._measure_times[n]
            except:
                print("Could not retrieve measured time at index ", n)
        else:
            try:
                return np.asarray(self._measure_times)
            except:
                print("could not retrieve measured time array")

    def set_pressure(self, n, p_level):
        try:
            self._pressure[n] = p_level
        except:
            print("The value is out of range to select pressure level")
    def init_pressure(self, pressure_array):
        try:
            self._pressure = pressure_array
        except:
            print("could not init pressure array")
    def get_pressure(self,n=None):
        if n is not None:
            try:
                return self._pressure[n]
            except:
                print("Could not retrieve pressure level at index ", n)
        else:
            try:
                return np.asarray(self._pressure)
            except:
                print("Could not retrieve pressure level array")

    def set_water_qty(self, n, cc):
        try:
            self._water_qty[n] = cc
        except:
            print("The value is out of range to for water qty")
    def init_water_qty(self, water_array):
        try:
            self._water_qty = water_array
        except:
            print("could not init water CC array")
    def get_water_qty(self,n=None):
        if n is not None:
            try:
                return self._water_qty[n]
            except:
                print("Could not retrieve water qty at index ", n)
        else:
            try:
                return self._water_qty
            except:
                print("Could not retrieve water qty array")

    def set_temp(self, n, t):
        try:
            self._temp[n] = t
        except:
            print("The value is out of range for temp")
    def init_temp(self, temp_array):
        try:
            self._temp = temp_array
        except:
            print("could not init temp array")
    def get_temp(self,n=None):
        if n is not None:
            try:
                return self._temp[n]
            except:
                print("Could not retrieve temp at index ", n)
        else:
            try:
                return np.asarray(self._temp)
            except:
                print("Could not retrieve temp array")

    def set_ambient_light_level(self, n, alm):
        try:
            self._ambient_light_level[n] = alm
        except:
            print("The value is out of range to select ambient light")
    def init_ambient_light_level(self, alm_array):
        try:
            self._ambient_light_level = alm_array
        except:
            print("could not init alm array")
    def get_ambient_light_level(self,n=None):
        if n is not None:
            try:
                return self._ambient_light_level[n]
            except:
                print("Could not retrieve ambient light at index ", n)
        else:
            try:
                return np.asarray(self._ambient_light_level)
            except:
                print("Could not retrieve ambient light array")

    def set_humidity(self, n, h):
        try:
            self._humidity[n] = h
        except:
            print("The value is out of range to select humidity")
    def init_humidity(self, humidity_array):
        try:
            self._humidity = humidity_array
        except:
            print("could not init alm array")
    def get_humidity(self,n=None):
        if n is not None:
            try:
                return self._humidity[n]
            except:
                print("Could not retrieve humidity index ", n)
        else:
            try:
                return np.asarray(self._humidity)
            except:
                print("Could not retrieve humidity array")

