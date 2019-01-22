import unittest
from Hackbright_coding_challenges import make_dict, is_anagram_of_palindrome


class TestMakeDict(unittest.TestCase):

    def test_make_dict(self):
        self.assertEqual(make_dict('hello'), {"h": 1, "e": 1, "l": 2, "o": 1})

    def test_is_anagram_of_palindrome(self):
    	self.assertTrue(is_anagram_of_palindrome("arceace"))
    	self.assertFalse(is_anagram_of_palindrome("arceaceb"))

if __name__ == '__main__':

	unittest.main()