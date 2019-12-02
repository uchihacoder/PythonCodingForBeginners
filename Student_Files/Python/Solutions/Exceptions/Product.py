# Solutions/Exceptions/Product.py
#

class Product:
    def __init__(self, prodNo, price):
        self.__prodNo = prodNo
        self.__price = price

    def setProdNo(self, prodNo):
        self.__prodNo = prodNo

    def setPrice(self, price):
        self.__price = price

    def getProdNo(self):
        return self.__prodNo

    def getPrice(self):
        return self.__price

    def __str__(self):
        return "{}: price={}".format( self.__prodNo, self.__price)