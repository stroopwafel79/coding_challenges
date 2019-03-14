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
        

class TestFurthest(unittest.TestCase):

    def test_furthest(self):
        self.assertEqual(furthest(3, [0, 1, 2]), 0)
        self.assertEqual(furthest(3, [2]), 2)
        self.assertEqual(furthest(3, [0]), 2)
        self.assertEqual(furthest(6, [2, 4]), 2)
        self.assertEqual(furthest(7, [0, 6]), 3)


### Example use of setUp and tearDown ###
# class WidgetTestCase(unittest.TestCase):
#     def setUp(self):
#         self.widget = Widget('The widget')

#     def tearDown(self):
#         self.widget.dispose()

### Unittest Methods ###
# assertEqual(a, b)           a == b   
# assertNotEqual(a, b)        a != b   
# assertTrue(x)               bool(x) is True  
# assertFalse(x)              bool(x) is False     
# assertIs(a, b)              a is b  
# assertIsNot(a, b)           a is not b  
# assertIsNone(x)             x is None   
# assertIsNotNone(x)          x is not None   
# assertIn(a, b)              a in b  
# assertNotIn(a, b)           a not in b  
# assertIsInstance(a, b)      isinstance(a, b)    
# assertNotIsInstance(a, b)   not isinstance(a, b)

if __name__ == '__main__':

    unittest.main()