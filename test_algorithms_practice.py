import unittest

from algorithms_practice import binary_search

# Create class with Test infront of what you're going to test
class TestBinarySearch(unittest.Testcase):

	# create function with test infront of what you're going to test
	def test_binary_search(self):
		nums_1 = [i for i in range(25)]
		nums_2 = [i for i in range(100000)]
		self.assertFalse(binary_search(50, nums_1))
		self.assertTrue(binary_search(5, nums_2))

if __name__ == '__main__':

	unittest.main()
