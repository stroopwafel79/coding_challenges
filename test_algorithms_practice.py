import unittest

from algorithms_practice import (sieve_of_eratosthenes, binary_search,
								 merge_sort)

# Create class with Test infront of what you're going to test
class SieveOfErastosthenes(unittest.TestCase):

	# create function with test infront of what you're going to test
	def test_sieve_of_eratosthenes(self):
		result_1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
		result_2 = [2, 3, 5, 7, 11, 13, 17, 19]
		result_3 = [2, 3, 5]
		self.assertEqual(sieve_of_eratosthenes(30), result_1)
		self.assertEqual(sieve_of_eratosthenes(20), result_2)
		self.assertEqual(sieve_of_eratosthenes(6), result_3)


class TestBinarySearch(unittest.TestCase):
	
	def test_binary_search(self):
		nums_1 = [i for i in range(25)]
		nums_2 = [i for i in range(100000)]
		self.assertFalse(binary_search(50, nums_1))
		self.assertTrue(binary_search(5, nums_2))


class TestMergeSort(unittest.TestCase):

	def test_merge_sort(self):
		lst_1 = [2, 8, 20, 1, 5]
		result_1 = [1, 2, 5, 8, 20]
		self.assertEqual(merge_sort(lst_1), result_1)

if __name__ == '__main__':

	unittest.main()


