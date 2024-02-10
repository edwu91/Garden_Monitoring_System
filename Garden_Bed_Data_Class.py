import numpy as np
from datetime import datetime
path = r"DataBaseID.txt"
class Garden_Bed_Data_Class:
    #This class is used to store all data belonging to one Bed.
    #this is all the data needed to describe what is monitored from the plant

    def __init__ (self, ID, name, date_start, day_elapse, day_remain):
#         exists = 0
#         try:
#             with open(path) as DB:
#                 number =[int(x) for x in DB]
#                 for i in number:
#                     if (ID == i):
#                         exists = 1
#                         print("ID already exists in database cannot create bed instance")
#             DB.close()
#             if (exists ==0):
#                 self._ID = ID
#                 self._name = name
#                 self._date_start = date_start
#                 self._days_elapsed = day_elapse
#                 self._days_remain = day_remain
#                 self._num_samples = 0
#                 self._measure_times = []
#                 self._moisture_level =[]
#                 self._water_qty = []
#                 self._temp = []
#                 self._ambient_light_level = []
#                 self._humidity = []
#                 DB = open("DataBaseID.txt", 'a')
#                 DB.write(str(ID))
#                 DB.write("\n")
#                 DB.close()
#         except:
#             print("error parsing DataBaseID.txt when initializing class")
        self._ID = []
        self._name = []
        self._date_start = []
        self._days_elapsed = []
        self._planting_time = []
        self._num_samples = []
        self._measure_times = []
        self._moisture_level =[]
        self._water_qty = []
        self._temp = []
        self._ambient_light_level = []
        self._humidity = []

    def init_ID(self, ID_array):
        try:
            self._ID = ID_array
        except:
            print("could not init num samples")
    def get_ID(self,n=None):
        if n is not None:
            return self._ID[n]
        else:
            return np.asarray(self._ID)

    def append_value(self, time, moisture_level, water_qty, temp, light_level, humidity):
        self._num_samples.append(1)
        #self._measure_times.append(time)
        self._moisture_level.append(moisture_level)
        self._water_qty.append(water_qty)
        self._temp.append(temp)
        self._ambient_light_level.append(light_level)
        self._humidity.append(humidity)

    def get_values_by_timestamp(self, n): #not thought out yet. 
        return [self._moisture_level[n], self._water_qty[n], self._temp[n], self._ambient_light_level[n], self._humidity[n]];

    def set_name(self,n,name):
        self._name[n] = name
    def init_name(self, name_array):
        self._name = name_array
    def get_name(self, n=None):
        if n is not None:
            return self._name[n]
        else:
            return np.asarray(self._name)

    def set_date_start(self, n,date_start):
        self._date_start[n] = date_start
    def init_date_start(self, date_start_array):
        self._date_start = date_start_array
    def get_date_start(self,n=None):
        if n is not None:
            return self._date_start[n]
        else:
            return np.asarray(self._date_start)

    def set_days_elapsed(self, n,days):
        self._days_elapsed[n] = days
    def init_days_elapsed(self, days_elapsed_array):
        self._days_elapsed = days_elapsed_array
    def get_days_elapsed(self, n=None):
        if n is not None:
            return self._days_elapsed[n]
        else:
            return np.asarray(self._days_elapsed)

    def set_planting_time(self, n, days):
        self._planting_time[n] = days
    def init_planting_time(self, planting_time_array):
        self._planting_time = planting_time_array
    def get_planting_time(self, n=None):
        if n is not None:
            return self._planting_time[n]
        else:
            return np.asarray(self._planting_time)
    def set_num_samples(self, n, n_value):
        try:
            self._num_samples[n] = n_value
        except:
            print("the value is out of range for num samples")
    def init_num_samples(self, n_array):
        try:
            self._num_samples = n_array
        except:
            print("could not init num samples")
    def get_num_samples(self, n=None):
        if n is not None:
            try:
                return self._num_samples[n]
            except:
                print("coud not retrieve sample num")
        else:
            try:
                return np.asarray(self._num_samples)
            except:
                print("could not retrieve num sample array")

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
                print("cant set time")
    def init_measure_times(self, time_array):
        try:
            #print("Bed init time")
            #print(datetime.strptime(time_array[0], "%Y-%m-%d %H:%M:%S"))
            self._measure_times = [datetime.strptime(s, "%Y-%m-%d %H:%M:%S") for s in time_array]
        except e:
            print(e)
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

    def set_moisture_level(self, n, m_level):
        try:
            self._moisture_level[n] = m_level
        except:
            print("The value is out of range to select moisture level")
    def init_moisture_level(self, moisture_array):
        try:
            self._moisture_level = moisture_array
        except:
            print("could not init moisture array")
    def get_moisture_level(self,n=None):
        if n is not None:
            try:
                return self._moisture_level[n]
            except:
                print("Could not retrieve moisture level at index ", n)
        else:
            try:
                #print([float(i) for i in self._moisture_level ])
                return np.asarray(self._moisture_level)
            except:
                print("Could not retrieve moisture level array")

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
                return self._temp
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
                return self._ambient_light_level
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
            print("could not init humidity array")
    def get_humidity(self,n=None):
        if n is not None:
            try:
                return self._humidity[n]
            except:
                print("Could not retrieve humidity index ", n)
        else:
            try:
                return self._humidity
            except:
                print("Could not retrieve humidity array")

