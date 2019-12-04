from Product import Product


class Internet(Product):
    def __init__(self, product_number, price, description, speed):
        self.set_product_number(product_number)
        self.set_price(price)
        self.__description = description
        self.__speed = speed

    def __str__(self):
        return f"product #: {self.get_product_number()}, price: {self.get_price()}, description: {self.__description}, speed: {self.__speed}"

    def verify(self):
        print(f"Verifying the speed is: {self.__speed} Mbps")
