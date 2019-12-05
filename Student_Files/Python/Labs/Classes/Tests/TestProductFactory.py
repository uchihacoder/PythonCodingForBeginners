import unittest
from ..ProductFactory import ProductFactory


class ProductFactoryTests(unittest.TestCase):
    def test_loadJSONProducts_should_load_data_from_file(self):
        # act
        products_from_file = ProductFactory.loadJSONProducts()

        # assert
        self.assertTrue(products_from_file)
        self.assertEqual(5, len(products_from_file))

    @unittest.skip("right now this is a LIVE test so skipping until we can mock MongoDB")
    def test_insertDBProducts_should_insert_products_into_mongodb(self):
        # act
        completed = ProductFactory.insertDBProducts()

        # assert
        self.assertTrue(completed)

    def test_queryDBProducts_should_retrieve_products_from_mongodb(self):
        # act
        products = ProductFactory.queryDBProducts()

        # assert
        self.assertTrue(products)
        self.assertEqual(4, len(products))


if __name__ == "__main__":
    unittest.main()
