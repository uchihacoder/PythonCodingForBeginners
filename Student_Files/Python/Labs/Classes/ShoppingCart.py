from IllegalArgumentException import IllegalArgumentException
from Cable import Cable
from Internet import Internet


class ShoppingCart:
    def __init__(self, name):
        self.__name = name
        self.__products = []

    def __str__(self):
        return f"name: {self.__name}, products:{self.__products}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def addProduct(self, product):
        # if ((type(product) is Cable) or (type(product) is Internet)):
        if type(product) is Cable or type(product) is Internet:
            self.__products.append(product)
        else:
            # TODO:  Print out the type(p) in the exception message
            raise IllegalArgumentException(
                f"{type(product)} Type is not allowed.")

    def remove_product(self, product):
        self.__products.remove(product)

    def listProducts(self):
        for product in self.__products:
            print(product)

    def getTotal(self):
        total = 0.00

        for product in self.__products:
            total += product.get_price()

        return total
