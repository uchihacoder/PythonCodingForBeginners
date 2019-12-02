import sys
import re
import os
from parse import *
from datetime import datetime
def printMenu():
    print("="*40)
    print("1) output hosts file")
    print("2) change IP address in hosts file (using re)")
    print("10) change current directory")
    print("11) output directory files")
    print("12) get file statistics")
    print("13) make directory")
    print("14) walk directories")
    print("15) get all environment variables")
    print("16) get individual environment variable")
    print("98) exit with 0 exit code")
    print("99) exit with -1 exit code")
    print("="*40)
def inputWithDefault(msg, defaultValue):
    msg = msg + " (" + defaultValue + ")>";
    val = input(msg);
    if not val:
        val = defaultValue;
    return val;
def outputHostsFile():
    host_fn = inputWithDefault("enter host filename", "hosts");
    with open(host_fn) as f:
        for line in f:
            print(line.rstrip())
def changeIPaddressHostsFile():
    ipaddress_in = inputWithDefault("enter input IP Address","127.0.0.1");
    ipaddress_out = inputWithDefault("enter output IP Address","127.0.0.2");
    fn_out  = inputWithDefault("enter revised host filename","hostsout");
    fin = open("hosts","r");
    fout = open(fn_out, "w+")
    while True:
        line = fin.readline();
        if not line:
            break;
        match = re.search("^" + ipaddress_in + " ", line);
        if match:
            line = re.sub(ipaddress_in, ipaddress_out, line);
        fout.write(line)
    fin.close();
    fout.close();
def changeCurrentDirectory():
    currentDir = os.getcwd();
    newDir = inputWithDefault("enter new directory",currentDir);
    if newDir != currentDir:
        os.chdir(newDir);
        print("current directory is now " + os.getcwd());
def outputDirectoryFiles():
    path = inputWithDefault("enter directory",os.getcwd());
    print("files in " + path + ":");
    fnames = os.listdir( path)
    for fname in fnames:
        print(fname)
def getFileStatistics():
    fname = inputWithDefault("enter filename", "hosts");
    stats = os.stat(fname);
    print(stats)
    print("Creation Date: " + str(datetime.fromtimestamp(stats.st_ctime)))
    print("Modification Date: " + str(datetime.fromtimestamp(stats.st_mtime)))
    print("File Size: " + str(stats.st_size) + " bytes")
def createDirectory():
    print("current directory is " + os.getcwd());
    dirName = input("enter directory to create>");
    dirName = os.getcwd() + "\\" + dirName;
    os.mkdir( dirName);
    #os.makedirs( dirName);
    print(dirName + " created");
def walkDirectories():
    curDir = os.getcwd()
    path = inputWithDefault("enter directory",curDir);
    for dpath, dnames, fnames in os.walk(path):
        print("Current Path:", dpath)
        print("Directories:", dnames)
        print("Files:", fnames)
        print()
def getEnvironmentVariables():
    envDict = os.environ
    for key in envDict.keys():
        print(key,envDict[key]);
def getEnvironmentVariable():
    envKey = inputWithDefault("enter enviroment variable name","SESSIONNAME");
    envValue = os.environ.get(envKey);
    print(str(envKey) + "=" + str(envValue));
while True:
    printMenu();
    cmd = input("Enter command>");
    if cmd == "98":
        sys.exit(0)
        # to read from windows: echo %errorlevel%
        # to read from unix: echo $?
    elif cmd == "99":
        sys.exit(-1)
        # to read from windows: echo %errorlevel%
        # to read from unix: echo $?
    elif cmd == "1":
        outputHostsFile();
    elif cmd == "2":
        changeIPaddressHostsFile();
    elif cmd == "3":
        pass;
    elif cmd == "10":
        changeCurrentDirectory();
    elif cmd == "11":
        outputDirectoryFiles();
    elif cmd == "12":
        getFileStatistics();
    elif cmd == "13":
        createDirectory();
    elif cmd == "14":
        walkDirectories();
    elif cmd == "15":
        getEnvironmentVariables();
    elif cmd == "16":
        getEnvironmentVariable();