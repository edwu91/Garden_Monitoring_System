import serial
import numpy as np

class sensors:
    def __init__(self):#consider adding serial port ID later
        self.ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) #baud changed from 9600 to 57600
        self.ser.flush()
        
    def get_all(self):
        self.ser.write(b"A\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        all_dat = np.array(line.split(";"))
        all_dat_float_array =np.asfarray(all_dat,float)
        if (all_dat_float_array[3]) ==0:
            all_dat_float_array[3] = 0.001
        all_dat_float_array[1] = all_dat_float_array[1]/1000.0
        return (all_dat_float_array)
    
    def get_temperature(self):
        self.ser.write(b"T\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        #print(type(line))
        #print(line)
        return float(line)

    def get_humidity(self):
        self.ser.write(b"H\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        return float(line)
    
    def get_pressure(self):
        self.ser.write(b"P\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        return float(line)/1000.0
    
    def get_lux(self):
        self.ser.write(b"L\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        if float(line) == 0.0:
            line = 0.001 #prevent the lux from being zero so that my precondition statement doesn't get invalidated
        return float(line)
    
    def get_moisture_s1(self):
        self.ser.write(b"M1\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        return float(line)/1000.0
    
    def get_moisture_s2(self):
        self.ser.write(b"M2\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        return float(line)/1000.0
    
    def get_moisture_s3(self):
        self.ser.write(b"M3\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        return float(line)/1000.0
    
    def get_moisture_s4(self):
        self.ser.write(b"M4\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        return float(line)/1000.0
    
    def pump1_on(self):
        self.ser.write(b"P1ON\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        return(line)
    
    def pump1_off(self):
        self.ser.write(b"P1OFF\n")
        line = self.ser.readline().decode('utf-8').rstrip()
        return (line)