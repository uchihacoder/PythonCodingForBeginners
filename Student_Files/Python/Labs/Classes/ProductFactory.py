import os
import re
from Product import Product
from Internet import Internet
from Cable import Cable


class ProductFactory:
    DATA_FILE_PATH = r"/Users/kevinjdonohue/GitHub/PythonCodingForBeginners/Student_Files/Python/Labs/Regex"

    @staticmethod
    # def getProducts():
    #     # products = [Product('1004X001', 50.00), Product('1004X001', 75.50) ]
    #     products = [
    #         Internet("1", 50.00, "Internet Desc", "50"),
    #         Cable("2", 2.00, "Cable Desc", "Cable Packages"),
    #         Product("3", 100.00)
    #     ]
    #     return products
    @staticmethod
    def extract_common_data(product_information):
        common = str(product_information[1]), format(
            float(product_information[2]), ".2f"), str(product_information[3])
        return common

    @staticmethod
    def create_internet_product(product_information):
        prod_no = str(product_information[1])

        valid_prod_no = re.search("^[0-9]{4}[A-Z]{1}[0-9]{3,4}$", prod_no)

        if not valid_prod_no:
            print(f"Product Number: {prod_no} is INVALID")

        price = format(float(product_information[2]), ".2f")
        desc = str(product_information[3])
        speed = format(float(product_information[4]), ".2f")

        return Internet(prod_no, price, desc, speed)

    @staticmethod
    def create_cable_product(product_information):
        prod_no = str(product_information[1])

        valid_prod_no = re.search("^[0-9]{4}[A-Z]{1}[0-9]{3,4}$", prod_no)

        if not valid_prod_no:
            print(f"Product Number: {prod_no} is INVALID")

        price = format(float(product_information[2]), ".2f")
        desc = str(product_information[3])
        packages = str(product_information[4]).rstrip().split(",")

        return Cable(prod_no, price, desc, packages)

    @staticmethod
    def getProducts():
        products = []

        data_file_path = ProductFactory.DATA_FILE_PATH

        os.chdir(data_file_path)

        print(f"reading from: {data_file_path}")

        with open("input_file_BadData.txt", "r") as file:
            while True:
                line = file.readline()

                print(line)

                if not line:
                    print(f"Something went wrong reading the line from the file.")
                    print(line)
                    break

                product_information = line.split("|")

                if product_information:
                    prod_no = str(product_information[1])
                    price = format(float(product_information[2]), ".2f")
                    desc = str(product_information[3])

                    if product_information[0] == "I":
                        products.append(
                            ProductFactory.create_internet_product(product_information))

                    elif product_information[0] == "C":
                        products.append(
                            ProductFactory.create_cable_product(product_information))

                    # TODO:  Since you didn't create a Phone class, leave this commented out from now
                    # elif product_information[0] == "P":
                    #     telephone_no = str(product_information[4])

                    #     new_product = Phone(prod_no, price, desc, telephone_no)

                    #     products.append(new_product)

        return products
