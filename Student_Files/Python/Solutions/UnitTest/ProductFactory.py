from Product import *
from Internet import *
from Cable import *
from Phone import *
import re
import json
import os
from pymongo import MongoClient

class ProductFactory:
    # TODO: modify the below path as necessary to 
    # navigate to the folder where the input_file.txt 
    # and Products.data files are located
    DATA_FILE_PATH = r"C:\Student_Files\Python\Labs\UnitTest";

    @staticmethod
    def getProducts():
        products = []
        os.chdir(ProductFactory.DATA_FILE_PATH);
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

    @staticmethod
    def loadJSONProducts():
        JSONproducts = []
        os.chdir(ProductFactory.DATA_FILE_PATH);
        print('reading from: ' + ProductFactory.DATA_FILE_PATH)
        productDataFile = open("Products.data", "r")
        for line in productDataFile:
            rawProduct = json.loads(line)
            JSONproducts.append( rawProduct)
        return JSONproducts

    # Open and insert records into the MongoDB database.
    @staticmethod
    def insertDBProducts():
        client = MongoClient()
        db = client.productsDB

        # Drop the products collection if it exists.
        db.products.drop()
        JSONproducts = ProductFactory.loadJSONProducts()

        for JSONproduct in JSONproducts:
            print("inserting into database:", JSONproduct)
            db.products.insert(JSONproduct)

        client.close()

    # Query records in the MongoDB database.
    @staticmethod
    def queryDBProducts():
        products = []
        client = MongoClient()
        db = client.productsDB

        # Drop the products collection if it exists.
        cursor = db.products.find()
        for JSONproduct in cursor:
            print("retrieved from database:", JSONproduct)
            prodNo = JSONproduct["prodNo"]
            price = float(JSONproduct["price"])
            desc = JSONproduct["desc"]
            if (JSONproduct["type"] == "I"):
                speed = float(JSONproduct["speed"])
                p = Internet( prodNo, price, desc, speed)
                products.append(p)
            elif (JSONproduct["type"] == "C"):
                packages = JSONproduct["packages"]
                p = Cable( prodNo, price, desc, packages)
                products.append(p)
            elif (JSONproduct["type"] == "P"):
                telNo = JSONproduct["telNo"]
                p = Phone( prodNo, price, desc, telNo)
                products.append(p)
        client.close()
        return products