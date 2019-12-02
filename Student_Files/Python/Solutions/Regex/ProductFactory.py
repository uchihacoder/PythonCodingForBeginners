from Product import *
from Internet import *
from Cable import *
from Phone import *
import re
import os

class ProductFactory:
    # TODO: modify the below path as necessary to 
    # navigate to the folder where the input_file.txt 
    # and input_file_BadData.txt fils are located
    DATA_FILE_PATH = r"C:\Student_Files\Python\Labs\Regex";

    @staticmethod
    def getProducts():
        products = []
        os.chdir(ProductFactory.DATA_FILE_PATH)
        print('reading from: ' + ProductFactory.DATA_FILE_PATH)
        with open('input_file_BadData.txt', 'r') as f:
            while True:
                line = f.readline()
                #print(line)
                if not line:
                    break
                s = line.split("|")
                prodNo = str(s[1])
                match = re.search('^\d{4}[A-Z]\d{3}$', prodNo)
                #print("line={}, match={}".format(line.rstrip(),prodNo))
                if not match:
                    print("ignoring:" + line.rstrip())
                    continue
                price = float(s[2])
                desc = s[3]
                if (s[0] == "I"):
                    speed = float(s[4])
                    p = Internet( prodNo, price, desc, speed)
                    products.append(p)
                elif (s[0] == "C"):
                    packages = (s[4].rstrip()).split(",")
                    p = Cable( prodNo, price, desc, packages)
                    products.append(p)
                elif (s[0] == "P"):
                    telNo = str(s[4])
                    p = Phone( prodNo, price, desc, telNo)
                    products.append(p)
            f.closed
        return products