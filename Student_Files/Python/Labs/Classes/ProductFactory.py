from Product import *


class ProductFactory:
    @staticmethod
    def getProducts():
        products = [Product('1004X001', 50.00), Product('1004X001', 75.50) ]
        return products