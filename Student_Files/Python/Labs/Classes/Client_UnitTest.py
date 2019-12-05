import unittest
import Client


class ClientTest(unittest.TestCase):
    def testProductLen(self):
        self.assertEqual(len(Client.products), 10,
                         "The number of products should equal 10")

    # def testTotal(self):
    #     self.assertEqual(Client.cart.getTotal(), 1000.00,
    #                      "The total should be 1,000.00")


if __name__ == "__main__":
    unittest.main()
