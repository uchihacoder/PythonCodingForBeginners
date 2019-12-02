from Internet import *
from Cable import *
from Phone import *
from Product import *

class ProductFactory:
    @staticmethod
    def getProducts():
        #products = [Product('1004X001', 50.00), Product('1004X001', 75.50) ]
        products = [Internet('1001I001', 60.00, 'Premium Internet', 100),
            Cable('1001C001', 80.00, 'Digital Cable', ['Sports', 'Family']),
            Phone('1001P001', 25.50, 'Standard Phone', '555-555-5555') ]
        return products