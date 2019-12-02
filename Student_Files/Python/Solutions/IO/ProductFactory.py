from Product import *
from Internet import *
from Cable import *
from Phone import *
import os

class ProductFactory:
    # TODO: modify the below path as necessary to 
    # navigate to the folder where the input_file.txt 
    # and input_file_BONUS.txt fils are located
    DATA_FILE_PATH = r"C:\Student_Files\Python\Labs\IO";
    
    @staticmethod
    def getProducts():
        products = []
        os.chdir(ProductFactory.DATA_FILE_PATH)
        print('reading from: ' + ProductFactory.DATA_FILE_PATH)
        with open('input_file.txt', 'r') as f:
            while True:
                line = f.readline()
                #print(line)
                if not line:
                    break
                s = line.split("|")
                prodNo = str(s[1])
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