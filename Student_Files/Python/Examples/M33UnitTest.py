import unittest;
def add( x, y):
	return x+y;

class SimpleTest( unittest.TestCase):
	def testadd1(self):
		self.assertEqual( add(2,5), 7);

if __name__ == '__main__':
	unittest.main();