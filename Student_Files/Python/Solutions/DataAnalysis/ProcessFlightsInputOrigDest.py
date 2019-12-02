import re
import numpy as np
import matplotlib as p
import pdb
from pandas import *
import os
        
while True:
    orig = input('Origin>')
    dest = input('Destination>')
    if ((re.search('^[A-Z]{3}$', orig) == None) or (re.search('^[A-Z]{3}$', dest) == None)):
        print("Invalid Orig/Dest (must be 3 character airport code)")
    else:
        break

DATA_FILE_PATH = r"C:\Student_Files\Python\Labs\DataAnalysis";
os.chdir(DATA_FILE_PATH)
print('reading from: ' + DATA_FILE_PATH)
print("Calculating flight information for {} to {} flights:".format(orig, dest))
df = read_csv('flight_info.csv')
orig_to_dest = df[(df.Origin == orig) & (df.Dest == dest)]
elapsed_time = orig_to_dest.ActualElapsedTime
print("number of {} to {} flights : {}".format(orig, dest,len(orig_to_dest)))
print("maximum elapsed time : {:>5.2f} hours".format(max(elapsed_time)/60))
print("minimum elapsed time : {:>5.2f} hours".format(min(elapsed_time)/60))
print("average elapsed time : {:>5.2f} hours".format(float(elapsed_time.sum()/len(elapsed_time))/60))
