import re
import os
print ("Current directory:" + str(os.getcwd()))
os.chdir(r"C:\Student_Files\Python\Examples");
print ("New directory:" + str(os.getcwd()))

def inputDefault( msg, default):
    val = input(msg + " (" + default + ")>")
    if val == "":
        val = default;
    return val;
fin = open("hosts");
outfn = inputDefault("output filename","hosts1")
fout = open(outfn,"w+")
intext = inputDefault("search for","12.200.15.")
outtext = inputDefault("replace with","12.200.16.")
while True:
    line = fin.readline();
    if not line:
        break;
    if re.search("^" +intext, line):
        line = re.sub(intext,outtext,line)
    fout.write(line);
fin.close();
fout.close();
