import os
from datetime import datetime
def printMenu():
    print("="*40);
    print("0) quit")
    print("1) output file")
    print("2) get file statistics")
    print("3) make directory")
    print("4) walk directories")
    print("5) remove directory")
    print("6) get all environment variables")
    print("7) get individual environment variable")
    print("8) change directory")
    print("9) list directory")
    print("10) show seps")
    print("="*40);
def inputDefault( msg, default):
    val = input(msg + " (" + default + ")>")
    if val == "":
        val = default;
    return val;
def outputFile():
    fname = inputDefault("enter filename","rhyme.txt");
    with open(fname) as f:
        for line in f:
            print(line.rstrip());
def getStatistics():
    fname = inputDefault("enter filename","rhyme.txt");
    stats = os.stat(fname);
    print(stats);
    print("file size in bytes:", stats.st_size)
    print("creation date:", datetime.fromtimestamp(stats.st_ctime))
    print("modification date:", datetime.fromtimestamp(stats.st_mtime))
    print("access date:", datetime.fromtimestamp(stats.st_atime))
def makeDirectory():
    curDir = os.getcwd();
    print("Current Directory:", curDir);
    dname = inputDefault("enter directory name","Whatever");
    if not os.path.exists(dname):
        os.mkdir(dname);
        #os.makedirs( dname);
def walkDirectory():
    curDir = os.getcwd();
    print("Current Directory:", curDir);
    dname = inputDefault("enter directory name",curDir);
    for path, dnames, fnames in os.walk(dname):
        print("Current Path:", path);
        print("Directories:", dnames);
        print("Files:", fnames);
        print();
def removeDirectory():
    curDir = os.getcwd();
    print("Current Directory:", curDir);
    dname = inputDefault("enter directory name","Whatever");
    if os.path.exists(dname):
        os.rmdir(dname);
def getEnvVar():
    ekey = inputDefault("enter environment variable name","HOMEPATH");
    eval = os.environ.get(ekey)
    print(ekey,"=",eval)
def getEnvVars():
    envDict = os.environ;
    print(envDict)
    for key in envDict.keys():
        print(key,"=",envDict[key])
def changeDirectory():
    curDir = os.getcwd();
    print("Current Directory:", curDir);
    dname = inputDefault("enter directory name", curDir);
    os.chdir(dname);
    print("New Current Directory:", os.getcwd());
def listDirectory():
    curDir = os.getcwd();
    print("Current Directory:", curDir);
    dname = inputDefault("enter directory name", curDir);
    fnames = os.listdir(dname);
    for fname in fnames:
        print(fname);
def showSeps():
    sep = os.sep;
    lsep = os.linesep;
    print(sep,lsep)
    path = str(sep) + "Student_Files" + str(sep) + "Python";
    print(path)
    os.chdir( path)
while True:
    printMenu();
    cmd = input("enter command>")
    if cmd == "0":
        break;
    elif cmd == "1":
        outputFile();
    elif cmd == "2":
        getStatistics();
    elif cmd == "3":
        makeDirectory();
    elif cmd == "4":
        walkDirectory();
    elif cmd == "5":
        removeDirectory();
    elif cmd == "6":
        getEnvVars();
    elif cmd == "7":
        getEnvVar();
    elif cmd == "8":
        changeDirectory();
    elif cmd == "9":
        listDirectory();
    elif cmd == "10":
        showSeps();
    else:
        print("invalid option")