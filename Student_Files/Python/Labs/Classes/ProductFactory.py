from Product import Product
from Internet import Internet
from Cable import Cable


class ProductFactory:
    @staticmethod
    def getProducts():
        # products = [Product('1004X001', 50.00), Product('1004X001', 75.50) ]
        products = [
            Internet("1", 50.00, "Internet Desc", "50"),
            Cable("2", 2.00, "Cable Desc", "Cable Packages"),
            Product("3", 100.00)
        ]
        return products
