import unittest
from Hackbright_coding_challenges import make_dict


class TestMakeDict(unittest.TestCase):

    def test_make_dict(self):
        self.assertEqual(make_dict('hello'), {"h": 1, "e": 1, "l": 2, "o": 1})

if __name__ == '__main__':

	unittest.main()