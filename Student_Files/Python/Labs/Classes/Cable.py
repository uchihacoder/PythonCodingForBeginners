from Product import Product


class Cable(Product):
    def __init__(self, product_number, price, description, packages):
        self.set_product_number(product_number)
        self.set_price(price)
        self.__description = description
        self.__packages = packages

    def __str__(self):
        return f"product #: {self.get_product_number()}, price: {self.get_price()}, description: {self.__description}, packages: {self.__packages}"

    def verify(self):
        print("Verifying the following packages: ", end=" ")

        for package in self.__packages:
            print(package, end=" ")

        print()
