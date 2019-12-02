# Solutions/Polymorphism/Phone.py
#

from Product import *
class Phone (Product):
    def __init__(self, prodNo, price, desc, telNo):
        self.setProdNo( prodNo)
        self.setPrice( price)
        self.__desc = desc
        self.__telNo = telNo

    def __str__(self):
        return "{}: price={}, desc={}, phone={}".format( self.getProdNo(),
                self.getPrice(), self.__desc, self.__telNo)

    def verify(self):
       print("Verifying your telephone number is : {}".format(self.__telNo))