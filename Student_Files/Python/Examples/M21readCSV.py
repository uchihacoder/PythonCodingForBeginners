#"Name", "Team", "Position", "Height(inches)", "Weight(lbs)", "Age"
import re
import os
print ("Current directory:" + str(os.getcwd()))
os.chdir(r"C:\Student_Files\Python\Examples");
print ("New directory:" + str(os.getcwd()))
with open("mlb_players.csv") as f:
    line = f.readline();
    line = re.sub('"',"",line)
    if line:
        header = line.split(",")
        len = len(header);
        for label in header:
            print(label, end="\t");
        print();
        for line in f:
            line = line.rstrip();
            line = re.sub('"', "", line)
            data = line.split(",");
            for label in data:
                print(label, end="\t");
            print();
