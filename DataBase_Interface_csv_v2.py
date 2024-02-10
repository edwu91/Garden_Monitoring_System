import csv
import pandas as pd
import numpy as np
import Garden_Bed_Data_Class as GB_Class
import Greenhouse_Data_Class as GH_Class
from datetime import datetime
save_path_GH = r"Greenhouse_save.csv"
save_path_GH_test = r"Greenhouse_save_test.csv"
save_path_GH_test = r"Greenhouse_save.csv"
save_path_bed1 = r"Bed1_save.csv"
save_path_bed2 = r"Bed2_save.csv"
save_path_bed3 = r"Bed3_save.csv"
save_path_bed4 = r"Bed4_save.csv"
save_path_bed_list = [save_path_bed1, save_path_bed2, save_path_bed3, save_path_bed4]
def load_data():

    df = pd.read_csv(save_path_GH) #encoding='utf-16'
    #print (df.dtypes)
    GH_inst = GH_Class.Greenhouse_Data_Class()
    GB_array = []
    #ambient_light
    gh_ambient_light = df.GH_LUX
    GH_inst.init_ambient_light_level(gh_ambient_light)
    #print(gh_ambient_light[0])
    #print(GH_inst.get_ambient_light_level())
    #GH days
    gh_days = df.GH_Days
    #print(gh_days)
    #print([datetime.strptime(s, "%Y-%m-%d %H:%M:%S") for s in gh_days])
    GH_inst.init_measure_times(gh_days)
    #GH_moisture
    gh_humidity = df.GH_Humidity
    GH_inst.init_humidity(gh_humidity)
    #Gh_temp
    gh_temp = df.GH_Temperature
    GH_inst.init_temp(gh_temp)
    #GH_Pressure
    gh_pressure = df.GH_Pressure
    GH_inst.init_pressure(gh_pressure)
    for file_to_read in save_path_bed_list:
        #print(file_to_read)
        df = pd.read_csv(file_to_read)
        bed = GB_Class.Garden_Bed_Data_Class(df.ID[0], df.Name[0], df["Date Started"][0], df["Days Elapsed"][0], df["Planting Time"][0])
        bed.init_ID(df.ID)
        bed.init_name(df.Name)
        bed.init_date_start(df["Date Started"])
        bed.init_days_elapsed(df["Days Elapsed"])
        bed.init_planting_time(df["Planting Time"])
        bed.init_measure_times(df.Days)
        bed.init_moisture_level(df.Humidity)
        bed.init_water_qty(df.Water)
        bed.init_temp(df.Temperature)
        GB_array.append(bed)
  
    return GH_inst, GB_array


####TEST SAVE DOES NOT WORK ANYMORE!!!!!!!!!!!!!!
###Need to change how bed is saved since now everything is an array.############
def test_save(): ####TEST SAVE DOES NOT WORK ANYMORE!!!!!!!!!!!!!!
    GH_Light_level = np.array([5001,6050,6020,5805,5250,6500,7005,5600,7500,6585,7550,6882,7003])
    GH_Humidity_level = np.array([0.554,0.543,0.453,0.5,0.495,0.487,0.532,0.484,0.608,0.599,0.495,0.440,0.441])
    GH_Temperature = np.array([25.2,26.7,24.8,20.9,26.6,25.6,23.4,27.7,27.8,24.5,24.6,23.3,22.2])
    GH_Pressure = np.array([101560,101700,100900,101420,101500,101579,101563,101589,101991,101123,101341,101123,101341])
    GH_Days = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
    df = pd.DataFrame({"GH_LUX" : GH_Light_level, "GH_Humdity" : GH_Humidity_level, "GH_Temperature" : GH_Temperature,
                      "GH_Pressure" : GH_Pressure, "GH_Days" : GH_Days})
#    df.to_csv(save_path_GH, index=False)

    #Bed1 = {0, "Leeks", "2021-02-14", 2, 12}
    Bed1_ID = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
    Bed1_name = np.array(["Leeks","Leeks","Leeks","Leeks","Leeks","Leeks","Leeks","Leeks","Leeks","Leeks","Leeks","Leeks","Leeks"])
    Bed1_date_started = np.array(["2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14","2021-02-14"])
    Bed1_days_elapsed = np.array([30,29,28,27,26,25,24,23,22,21,20,19,18])
    Bed1_planting_time = np.array([50,50,50,50,50,50,50,50,50,50,50,50,50]) 
    Bed1_data = np.array([0.664,0.682,0.599,0.576,0.681,0.666,0.685,0.594,0.575,0.566,0.594,0.555,0.577])
    Bed1_water = np.array([0,0,0,0,10,0,0,0,0,0,0,0,0])
    Bed1_temp = np.array([25.2,26.7,24.8,20.9,26.6,25.6,23.4,27.7,27.8,24.5,24.6,23.3,22.2])
    Bed1_days = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
    Bed1_df = pd.DataFrame({"ID" : Bed1_ID, "Name" : Bed1_name, "Date Started" : Bed1_date_started, "Days Elapsed" : Bed1_days_elapsed, "Planting Time" : Bed1_planting_time,
                            "Humidity" : Bed1_data, "Water" : Bed1_water, "Temperature" : Bed1_temp ,"Days" : Bed1_days})
    Bed1_df.to_csv(save_path_bed1, index=False)
#    Bed2_data = np.array([0.598,0.655,0.576,0.681,0.666,0.554,0.595,0.594,0.589,0.61,0.601,0.666,0.685])
#    Bed2_water = np.array([0,0,0,0,10,0,0,0,0,0,0,0,0])
#    Bed2_temp = np.array([25.2,26.7,24.8,20.9,26.6,25.6,23.4,27.7,27.8,24.5,24.6,23.3,22.2])
#    Bed2_days = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
#    Bed2_df = pd.DataFrame({"ID" : 1, "Name" : "Parsley", "Date Started" : "2021-02-20", "Days Elapsed" : 24, "Planting Time" : 80,
#                            "Humidity" : Bed2_data,  "Water" : Bed2_water, "Temperature" : Bed2_temp , "Days" : Bed2_days})
#    Bed2_df.to_csv(save_path_bed2, index=False)
#    Bed3_data = np.array([0.64,0.704,0.685,0.684,0.681,0.666,0.554,0.595,0.595,0.594,0.589,0.691,0.7])
#    Bed3_water = np.array([0,0,0,0,10,0,0,0,0,0,0,0,0])
#    Bed3_temp = np.array([25.2,26.7,24.8,20.9,26.6,25.6,23.4,27.7,27.8,24.5,24.6,23.3,22.2])
#    Bed3_days = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
#    Bed3_df = pd.DataFrame({"ID" : 2, "Name" : "Cauliflower", "Date Started" : "2021-03-20", "Days Elapsed" : 1, "Planting Time" : 100,
#                            "Humidity" : Bed3_data, "Water" : Bed3_water, "Temperature" : Bed3_temp , "Days" : Bed3_days})
#    Bed3_df.to_csv(save_path_bed3, index=False)
#    Bed4_data = np.array([0.631,0.695,0.635,0.687,0.681,0.681,0.575,0.562,0.575,0.566,0.594,0.555,0.577])
#    Bed4_water = np.array([0,0,0,0,10,0,0,0,0,0,0,0,0])
#    Bed4_temp = np.array([25.2,26.7,24.8,20.9,26.6,25.6,23.4,27.7,27.8,24.5,24.6,23.3,22.2])
#    Bed4_days = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
#    Bed4_df = pd.DataFrame({"ID" : 3, "Name" : "Bush Beans", "Date Started" : "2021-03-20", "Days Elapsed" : 1, "Planting Time" : 100,
#                            "Humidity" : Bed4_data, "Water" : Bed4_water, "Temperature" : Bed4_temp , "Days" : Bed4_days})
#    Bed4_df.to_csv(save_path_bed4, index=False)
    return 1

def save_GH_data(GH_inst):
    return 1

def save_all_bed_data(GH_inst, GB_Array):
    
    return 1

    
def save_all(GH, GB_Array):
    #Greenhouse Data
    #print([x.strftime("%Y-%m-%d %H:%M:%S") for x in GH.get_measure_times()])
    df = pd.DataFrame({"GH_LUX" : GH.get_ambient_light_level(), "GH_Humidity" : GH.get_humidity(),
                       "GH_Temperature" : GH.get_temp(), "GH_Pressure" : GH.get_pressure(), "GH_Days" : [x.strftime("%Y-%m-%d %H:%M:%S") for x in GH.get_measure_times()]})
    df.to_csv(save_path_GH, index=False)

    #bed data
    for i in range (0,4):# in save_path_bed_list:
        #print(GB_Array[i].get_ID())
        #print(GB_Array[i].get_name())
        #print(GB_Array[i].get_date_start())
        #print(GB_Array[i].get_days_elapsed())
        #print(GB_Array[i].get_planting_time())
        #print(GB_Array[i].get_moisture_level())
        #print(GB_Array[i].get_water_qty())
        #print(GB_Array[i].get_temp())
        #print(GB_Array[i].get_measure_times())
        Bed_df = pd.DataFrame({"ID" : GB_Array[i].get_ID(), "Name" : GB_Array[i].get_name(), "Date Started" : GB_Array[i].get_date_start(),
                               "Days Elapsed" : GB_Array[i].get_days_elapsed(), "Planting Time" : GB_Array[i].get_planting_time(),
                               "Humidity" : GB_Array[i].get_moisture_level(), "Water" : GB_Array[i].get_water_qty(),
                               "Temperature" : GB_Array[i].get_temp() ,"Days" : [x.strftime("%Y-%m-%d %H:%M:%S") for x in GB_Array[i].get_measure_times()]})
        Bed_df.to_csv(save_path_bed_list[i], index=False)
        print("saved the following: ", save_path_bed_list[i])
    return 1

#ts = test_save()
#gh, bed_arr = load_data()

