import re
import numpy as np
import matplotlib as p
import pdb
import os
from pandas import *

while True:
    orig = input('Origin>')
    dest = input('Destination>')
    if ((re.search('^[A-Z]{3}$', orig) == None) or (re.search('^[A-Z]{3}$', dest) == None)):
        print("Invalid Orig/Dest (must be 3 character airport code)")
    else:
        break

# DATA_FILE_PATH = r"C:\Student_Files\Python\Labs\DataAnalysis"
DATA_FILE_PATH = r"/Users/kevinjdonohue/GitHub/PythonCodingForBeginners/Student_Files/Python/Labs/DataAnalysis"

os.chdir(DATA_FILE_PATH)
print('reading from: ' + DATA_FILE_PATH)
print("Calculating flight information for {} to {} flights:".format(orig, dest))

flight_info_from_csv = pandas.read_csv("flight_info.csv")

# NOTE:  Use & instead of Python "and" because we are actually doing a bitwise operation (apparently)
origin_to_destination = flight_info_from_csv[(
    flight_info_from_csv.Origin == orig) & (flight_info_from_csv.Dest == dest)]

# print(origin_to_destination)

elapsed_time = origin_to_destination.ActualElapsedTime

# print(elapsed_time)

print(f"number of {orig} to {dest} flights: {len(origin_to_destination)}")

max_elapsed_time_hours = max(elapsed_time) / 60

min_elapsed_time_hours = min(elapsed_time) / 60

# average_elapsed_time_hours = (elapsed_time)/len(elapsed_time)

# print(f"elapsed time:\n {elapsed_time}")

print(f"maximum elapsed time (in hours): {max_elapsed_time_hours}")

print(f"minimum elapsed time (in hours): {min_elapsed_time_hours}")

# print(f"average elapsed time (in hours): {average_elapsed_time_hours}")
