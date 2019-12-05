import unittest


class Calculator(object):

    def add(self, x, y):
        return x + y


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.__calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.__calculator.add(2, 3), 5,
                         "two plus three should be five")

    def test_add_0(self):
        self.assertEqual(self.__calculator.add(0, 0), 0,
                         "zero plus zero should be zero")


if __name__ == "__main__":
    unittest.main()
