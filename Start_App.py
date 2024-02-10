from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction,QWidget
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from pyqtgraph.Qt import QtCore, QtGui
import os
import sys
import time
import numpy as np
from datetime import datetime
from random import uniform
from Sensor.sensors import sensors
import DataBase_Interface_csv_v2 as Database
import Garden_Bed_Data_Class as bed_class
import Greenhouse_Data_Class as GH_class

from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QUrl

#tracking interval
INTERVAL = 2400000 #in msec

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #picture
        #pic = QtGui.QLabel(window)
        #pic.setGeometry(10, 10, 400, 100)
        #use full ABSOLUTE path to the image, not relative
        #pic.setPixmap = (QtGui.QPixmap(os.getcwd() + "/testimg.jpg"))
        self.mainMenu = self.menuBar()      # Menu bar
        openAction = QAction('&Open', self)
        saveAction = QAction ('&Save', self)
        exitAction = QAction('&Exit', self)
        openAction.setShortcut('Ctrl+O')
        saveAction.setShortcut('Ctrl+S')
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        self.fileMenu = self.mainMenu.addMenu('&File')
        self.fileMenu.addAction(exitAction)
        
        
        GH_temp_style = {'font-weight':'bold', 'font-size':'60px'}
        title = QtGui.QLabel("Greenhouse Monitor")
        title.setFont(QtGui.QFont('Arial', 60))
        self.img = (QtGui.QPixmap(os.getcwd() + "/greenhouse_pic.JPG").scaled(444,297))
        #rect = QtGui.QRect(10,20,30,40)
        #self.img_cropped = QtGui.QPixamp(self.img.copy(rect)
        self.label = QtGui.QLabel()
        self.label.setPixmap(self.img)
        #self.label.setGeometry(10,10,400,100)
        
        #webcam
        self.webcam = QWebView()
        self.webcam.setUrl( QUrl("http://192.168.1.77/html/") )
        #self.webcam.setGeometry(20,20,400,100)
        self.sensors = sensors()
        self.load_data()
        self.init_graphs()
        self.init_bd_widgets()
        self.init_gh_widgets()
       
        layout = QtWidgets.QGridLayout()
        #layout.addWidget(title,0,0)#title label
        layout.addWidget(self.label,0,0,QtCore.Qt.AlignCenter)
        layout.addWidget(self.obj1,0,1)
        layout.addWidget(self.obj2,1,1)
        layout.addWidget(self.obj3,2,1)
        layout.addWidget(self.obj4,3,1)
        layout.addWidget(self.obj5,0,2)
        layout.addWidget(self.subframe1_box,0,3)        #description
        layout.addWidget(self.obj6,1,2)
        layout.addWidget(self.subframe2_box,1,3)        #description
        layout.addWidget(self.obj7,2,2)
        layout.addWidget(self.subframe3_box,2,3)        #description
        layout.addWidget(self.obj8,3,2)
        layout.addWidget(self.subframe4_box,3,3)        #description
        
        #label for application
        #layout.addWidget(self.label,1,0,2,1)  #image
        layout.addWidget(self.webcam,1,0,2,1) #webcam
        layout.addWidget(self.subframe_gh_box,3,0)
        #get update, water all
        box = QtWidgets.QGroupBox(self)
        box.setLayout(layout)
        self.setCentralWidget(box)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(INTERVAL)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
    
    def load_data(self):
        self.BD_array =[]
        self.greenhouse = GH_class.Greenhouse_Data_Class()
        self.greenhouse, self.BD_array = Database.load_data()
        
    def init_graphs(self):
        #self.GH_days = list(range(10))
        #self.GH_temperature = [uniform(19.0,20.1) for _ in range (10)]
        #self.GH_pressure = [uniform(101,101.5) for _ in range(10)]
        #self.GH_humidity = [uniform(47.5,48.5) for _ in range(10)]
        #self.GH_LUX = [uniform(100,300) for _ in range(10)]
        # Bed data:
        self.BD1_days = self.BD_array[0].get_measure_times()
        self.BD1_moisture = self.BD_array[0].get_moisture_level()
        self.BD1_name = self.BD_array[0].get_name()
        self.BD1_ID = self.BD_array[0].get_ID()
        self.BD1_date_start = self.BD_array[0].get_date_start()
        self.BD1_days_elapsed = self.BD_array[0].get_days_elapsed()
        self.BD1_planting_time = self.BD_array[0].get_planting_time()
        self.BD1_water = self.BD_array[0].get_water_qty()
        self.BD1_temp = self.BD_array[0].get_temp()
        
        #greenhouse data
        self.GH_days = self.greenhouse.get_measure_times()
        self.GH_temperature = self.greenhouse.get_temp()
        self.GH_pressure = self.greenhouse.get_pressure()
        self.GH_humidity = self.greenhouse.get_humidity()
        self.GH_LUX = self.greenhouse.get_ambient_light_level()
        date_axis1 = pg.DateAxisItem(orientation='bottom')
        date_axis2 = pg.DateAxisItem(orientation='bottom')
        date_axis3 = pg.DateAxisItem(orientation='bottom')
        date_axis4 = pg.DateAxisItem(orientation='bottom')
        date_axis5 = pg.DateAxisItem(orientation='bottom')
        date_axis6 = pg.DateAxisItem(orientation='bottom')
        date_axis7 = pg.DateAxisItem(orientation='bottom')
        date_axis8 = pg.DateAxisItem(orientation='bottom')
        self.obj1 = pg.PlotWidget(axisItems = {'bottom': date_axis1}) #GH temperature plot
        self.obj2 = pg.PlotWidget(axisItems = {'bottom': date_axis2}) #GH pressure plot
        self.obj3 = pg.PlotWidget(axisItems = {'bottom': date_axis3}) #GH humidity plot
        self.obj4 = pg.PlotWidget(axisItems = {'bottom': date_axis4}) #GH lux plot
        self.obj5 = pg.PlotWidget(axisItems = {'bottom': date_axis5}) #bed plot 1 -> have both moisture and water amount on same graph
        self.obj6 = pg.PlotWidget(axisItems = {'bottom': date_axis6}) #bed plot 2 -> change this to bed temperature for now:
        self.obj7 = pg.PlotWidget(axisItems = {'bottom': date_axis7}) #bed plot 3
        self.obj8 = pg.PlotWidget(axisItems = {'bottom': date_axis8}) #bed plot 4
        self.obj1.setBackground(QtGui.QColor(220,220,220,185))#light grey
        self.obj2.setBackground(QtGui.QColor(220,220,220,185))#light grey
        self.obj3.setBackground(QtGui.QColor(220,220,220,185))#light grey
        self.obj4.setBackground(QtGui.QColor(220,220,220,185))#light grey
        self.obj5.setBackground(QtGui.QColor(220,220,220,185))#light grey
        self.obj6.setBackground(QtGui.QColor(220,220,220,185))#light grey
        self.obj7.setBackground(QtGui.QColor(220,220,220,185))#light grey
        self.obj8.setBackground(QtGui.QColor(220,220,220,185))#light grey
        GH_temp_style = {'color':'r', 'font-size':'20px'}
        GH_pressure_style = {'color':'orange', 'font-size':'20px'}
        GH_humidity_style = {'color':'blue', 'font-size':'20px'}
        GH_LUX_style = {'color':'purple', 'font-size':'20px'}
        BD_moisture_style = {'color':'r', 'font-size':'20px'}
        self.obj1.setLabel('left', 'Temperature (°C)', **GH_temp_style)
        self.obj1.setLabel('bottom', 'Hour (H)', **GH_temp_style)
        self.obj2.setLabel('left', 'Pressure (kPa)', **GH_pressure_style)
        self.obj2.setLabel('bottom', 'Hour (H)', **GH_pressure_style)
        self.obj3.setLabel('left', 'Humidity (%)', **GH_humidity_style)
        self.obj3.setLabel('bottom', 'Hour (H)', **GH_humidity_style)
        self.obj4.setLabel('left', 'Ligh Level (LUX)', **GH_LUX_style)
        self.obj4.setLabel('bottom', 'Hour (H)', **GH_LUX_style)
        self.obj5.setLabel('left', 'Bed 1 Moisture (%)', **BD_moisture_style)
        self.obj5.setLabel('bottom', 'Hour (H)', **BD_moisture_style)
        self.obj6.setLabel('left', 'Bed 2 Moisture (%)', **BD_moisture_style)
        self.obj6.setLabel('bottom', 'Hour (H)', **BD_moisture_style)
        self.obj7.setLabel('left', 'Bed 3 Moisture (%)', **BD_moisture_style)
        self.obj7.setLabel('bottom', 'Hour (H)', **BD_moisture_style)
        self.obj8.setLabel('left', 'Bed 4 Moisture (%)', **BD_moisture_style)
        self.obj8.setLabel('bottom', 'Hour (H)', **BD_moisture_style)      
        
        #insert bed values. 
        
        # plot data: x, y values
        pen_temp = pg.mkPen(color=(255,10,10),width=5)
        pen_pressure = pg.mkPen(color=(255,165,0),width=5)
        pen_humidity = pg.mkPen(color=(50,50,200),width=5)
        pen_LUX = pg.mkPen(color=(200,000,200),width=5)
        pen_bed = pg.mkPen(color=(0,255,0),width=4)
        

        self.data_line1 = self.obj1.plot(x=[x.timestamp() for x in self.GH_days], y=self.GH_temperature,pen=pen_temp, symbol='o', symbolSize=10, symbolBrush=(255,10,10))
        self.data_line2 = self.obj2.plot(x=[x.timestamp() for x in self.GH_days], y=self.GH_pressure,pen=pen_pressure, symbol='o', symbolSize=10, symbolBrush=(255,165,0))
        self.data_line3 = self.obj3.plot(x=[x.timestamp() for x in self.GH_days], y=self.GH_humidity,pen=pen_humidity, symbol='o', symbolSize=10, symbolBrush=(50,50,200))
        self.data_line4 = self.obj4.plot(x=[x.timestamp() for x in self.GH_days], y=self.GH_LUX,pen=pen_LUX, symbol='o', symbolSize=10, symbolBrush=(200,000,200))
        self.data_line5 = self.obj5.plot(x=[x.timestamp() for x in self.BD1_days], y=self.BD1_moisture, pen=pen_bed, symbol='o', symbolSize=10, symbolBrush=(0,255,0))
    
    def init_bd_widgets(self):
        subframe1_layout = QtWidgets.QGridLayout()
        self.bed1_water_button = QtGui.QPushButton("Water")
        self.bed1_water_button.clicked.connect(self.water_bed)
        self.bed1_info = "Plant name:" + str(self.BD1_name[0]) + "\nDate Started: " + str(self.BD1_date_start[0]) +"\nNum days to maturity: " + str(self.BD1_planting_time[0])
        self.bed1_label = QtGui.QLabel(self.bed1_info)
        self.bed1_update_button = QtGui.QPushButton("Update")
        self.bed1_update_button.clicked.connect(self.update_bed_data)
        subframe1_layout.addWidget(self.bed1_water_button,0,0)
        subframe1_layout.addWidget(self.bed1_label,1,0)
        subframe1_layout.addWidget(self.bed1_update_button,2,0)
        self.subframe1_box = QtWidgets.QGroupBox()
        self.subframe1_box.setLayout(subframe1_layout)
        
        subframe2_layout = QtWidgets.QGridLayout()
        self.bed2_water_button = QtGui.QPushButton("Water")
        self.bed2_info = "Bed 2 info"
        self.bed2_label = QtGui.QLabel(self.bed2_info)
        self.bed2_update_button = QtGui.QPushButton("Update")
        subframe2_layout.addWidget(self.bed2_water_button,0,0)
        subframe2_layout.addWidget(self.bed2_label,1,0)
        subframe2_layout.addWidget(self.bed2_update_button,2,0)
        self.subframe2_box = QtWidgets.QGroupBox()
        self.subframe2_box.setLayout(subframe2_layout)        
        
        subframe3_layout = QtWidgets.QGridLayout()
        self.bed3_water_button = QtGui.QPushButton("Water")
        self.bed3_info = "Bed 3 info"
        self.bed3_label = QtGui.QLabel(self.bed3_info)
        self.bed3_update_button = QtGui.QPushButton("Update")
        subframe3_layout.addWidget(self.bed3_water_button,0,0)
        subframe3_layout.addWidget(self.bed3_label,1,0)
        subframe3_layout.addWidget(self.bed3_update_button,2,0)
        self.subframe3_box = QtWidgets.QGroupBox()
        self.subframe3_box.setLayout(subframe3_layout)
        
        subframe4_layout = QtWidgets.QGridLayout()
        self.bed4_water_button = QtGui.QPushButton("Water")
        self.bed4_info = "Bed 4 info"
        self.bed4_label = QtGui.QLabel(self.bed4_info)
        self.bed4_update_button = QtGui.QPushButton("Update")
        subframe4_layout.addWidget(self.bed4_water_button,0,0)
        subframe4_layout.addWidget(self.bed4_label,1,0)
        subframe4_layout.addWidget(self.bed4_update_button,2,0)
        self.subframe4_box = QtWidgets.QGroupBox()
        self.subframe4_box.setLayout(subframe4_layout)
        
    def init_gh_widgets(self):
        subframe_gh_layout = QtWidgets.QGridLayout()
        self.gh_update_button = QtGui.QPushButton("Update")
        self.gh_update_button.clicked.connect(self.update_GH_data)
        self.gh_save_button = QtGui.QPushButton("Save")
        self.gh_save_button.clicked.connect(self.save_data)
        self.gh_water_all_button = QtGui.QPushButton("Water All")
        subframe_gh_layout.addWidget(self.gh_update_button,0,0)
        subframe_gh_layout.addWidget(self.gh_water_all_button,0,1)
        subframe_gh_layout.addWidget(self.gh_save_button,0,2)
        self.subframe_gh_box = QtWidgets.QGroupBox()
        self.subframe_gh_box.setLayout(subframe_gh_layout)
    
    def save_data(self):
        print('saving data')
        self.greenhouse.set_measure_times(n=None,time=self.GH_days)
        self.greenhouse.init_pressure(self.GH_pressure)
        self.greenhouse.init_temp(self.GH_temperature)
        self.greenhouse.init_humidity(self.GH_humidity)
        self.greenhouse.init_ambient_light_level(self.GH_LUX)
        
        self.BD_array[0].set_measure_times(n=None, time=self.BD1_days)
        self.BD_array[0].init_moisture_level(self.BD1_moisture)
        self.BD_array[0].init_name(self.BD1_name)
        self.BD_array[0].init_ID(self.BD1_ID)
        self.BD_array[0].init_date_start(self.BD1_date_start)
        self.BD_array[0].init_days_elapsed(self.BD1_days_elapsed)
        self.BD_array[0].init_planting_time(self.BD1_planting_time)
        self.BD_array[0].init_water_qty(self.BD1_water)
        self.BD_array[0].init_temp(self.BD1_temp)
        Database.save_all(self.greenhouse,self.BD_array)
        print('data saved')
        #put all data in the gui specific variables into the GH and BED class
        
        
        
    def update_GH_data(self):
        #start = time.time()
        all_vals = self.sensors.get_all()
        temp = all_vals[0]
        pressure = all_vals[1]
        humidity = all_vals[2]
        LUX = all_vals[3]
        #temp = self.sensors.get_temperature()
        #pressure = self.sensors.get_pressure()
        #humidity = self.sensors.get_humidity()
        #LUX = self.sensors.get_lux()
        
        #end = time.time()
        #delta = end - start
        #print("time taken to collect GH data: ", delta)
        if (not(temp) or not(pressure) or not(humidity) or not(LUX)):
            print(temp)
            print(pressure)
            print(humidity)
            print(LUX)
            print("one of the greenhouse values is reading zero or invalid data")
        else:
            #self.GH_days = np.append(self.GH_days,self.GH_days[-1] + 1)  # Add a new value 1 higher than the last.
            self.GH_days = np.append(self.GH_days,datetime.today())
            
            self.GH_temperature=np.append(self.GH_temperature,temp)
            self.GH_pressure=np.append(self.GH_pressure,pressure)
            self.GH_humidity=np.append(self.GH_humidity,humidity)
            self.GH_LUX=np.append(self.GH_LUX,LUX)

            self.data_line1.setData(x=[x.timestamp() for x in self.GH_days], y=self.GH_temperature)  # Update the data.
            self.data_line2.setData(x=[x.timestamp() for x in self.GH_days], y=self.GH_pressure)
            self.data_line3.setData(x=[x.timestamp() for x in self.GH_days], y=self.GH_humidity)
            self.data_line4.setData(x=[x.timestamp() for x in self.GH_days], y=self.GH_LUX)
        
    def update_bed_data(self):
        moisture = self.sensors.get_moisture_s1()
        print(moisture)
        self.BD1_name = np.append(self.BD1_name,self.BD1_name[-1])
        self.BD1_ID = np.append(self.BD1_ID,self.BD1_ID[-1])
        self.BD1_date_start = np.append(self.BD1_date_start,self.BD1_date_start[-1])
        self.BD1_days_elapsed = np.append(self.BD1_days_elapsed,self.BD1_days_elapsed[-1])
        self.BD1_planting_time = np.append(self.BD1_planting_time,self.BD1_planting_time[-1])
        #self.BD1_days = np.append(self.BD1_days,self.BD1_days[-1] + 1)
        self.BD1_days = np.append(self.BD1_days,datetime.today())
        
        self.BD1_moisture = np.append(self.BD1_moisture,moisture)
        self.BD1_temp = np.append(self.BD1_temp, self.sensors.get_temperature())
        self.data_line5.setData(x=[x.timestamp() for x in self.BD1_days], y=self.BD1_moisture)
        if (moisture < 0.19): #this is the number used to determine if the plants need more water. 
            self.water_bed()
            self.BD1_water = np.append(self.BD1_water,1)
        else:
            self.BD1_water = np.append(self.BD1_water,0)
    
    def water_bed(self):
        self.sensors.pump1_on()
        time.sleep(15) #this can be done better. 
        self.sensors.pump1_off()
        
    
    def update_plot_data(self):
        minute_timestamp = INTERVAL
        self.update_GH_data()
        self.update_bed_data()
        self.save_data()
        

       
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    



if __name__ == '__main__':
    main()