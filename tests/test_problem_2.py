import unittest
from .context import src


class TestProblem2(unittest.TestCase):

    def test_find_palindroms_abc(self):
        result = src.find_palindroms_str("abc")
        match = ['a', 'b', 'c']
        self.assertListEqual(result, match)

    def test_find_palindroms_racerannakayak(self):
        result = src.find_palindroms_str("racecarannakayak")
        match = ['racecar', 'anna', 'kayak']
        self.assertListEqual(result, match)

    def test_find_palindroms_noneinput(self):
        with self.assertRaises(Exception):
            src.find_palindroms_str(None)


if __name__ == '__main__':
    unittest.main()
