import numpy as np
import matplotlib as p
import pdb
from pandas import *
import os

DATA_FILE_PATH = r"C:\Student_Files\Python\Labs\DataAnalysis";
os.chdir(DATA_FILE_PATH)
print('reading from: ' + DATA_FILE_PATH)
print("Calculating flight information for LAX to DFW flights:")
df = read_csv('flight_info.csv')
lax_to_dfw = df[(df.Origin == "LAX") & (df.Dest == "DFW")]
elapsed_time = lax_to_dfw.ActualElapsedTime
print("number of LAX to DFW flights : {}".format(len(lax_to_dfw)))
print("maximum elapsed time : {:>5.2f} hours".format(max(elapsed_time)/60))
print("minimum elapsed time : {:>5.2f} hours".format(min(elapsed_time)/60))
print("average elapsed time : {:>5.2f} hours".format(float(elapsed_time.sum()/len(elapsed_time))/60))
