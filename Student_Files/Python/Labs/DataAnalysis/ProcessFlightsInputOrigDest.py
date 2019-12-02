import re
import numpy as np
import matplotlib as p
import pdb
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
# code goes here