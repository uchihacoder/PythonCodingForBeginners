class Product:
    def __init__(self, product_number, price):
        self.__product_number = product_number
        self.__price = price

    def __str__(self):
        return f"product#: {self.__product_number}, price: {self.__price}"

    def get_product_number(self):
        return self.__product_number

    def set_product_number(self, product_number):
        self.__product_number = product_number

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def print(self):
        print("Testing access to Product functions")
