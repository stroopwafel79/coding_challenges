import unittest
from Hackbright_coding_challenges import (make_dict, is_anagram_of_palindrome,
                                          count_recursively, sum_list)


class TestMakeDict(unittest.TestCase):

    def test_make_dict(self):
        self.assertEqual(make_dict('hello'), {"h": 1, "e": 1, "l": 2, "o": 1})

    
class TestAnagramOfPalindrome(unittest.TestCase):

    def test_is_anagram_of_palindrome(self):
        self.assertTrue(is_anagram_of_palindrome("arceace"))
        self.assertFalse(is_anagram_of_palindrome("arceaceb"))

class TestCountRecursively(unittest.TestCase):

    def test_count_recursively(self):
        self.assertEqual(count_recursively([1, 2, 3]), 3)
        self.assertEqual(count_recursively([]), 0)


class TestSumRecursively(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(sum_list([5, 5]), 10)
        self.assertEqual(sum_list([-5, 10, 4]), 9)
        self.assertEqual(sum_list([20]), 20)
        self.assertEqual(sum_list([]), 0)
    

if __name__ == '__main__':

    unittest.main()