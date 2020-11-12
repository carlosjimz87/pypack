import unittest
from .context import problems


class TestProblem2(unittest.TestCase):

    def test_palindromes_problem_abc(self):
        result = problems.palindromes_problem("abc")
        match = ['a', 'b', 'c']
        self.assertListEqual(result, match)

    def test_palindromes_problem_racerannakayak(self):
        result = problems.palindromes_problem("racecarannakayak")
        match = ['racecar', 'anna', 'kayak']
        self.assertListEqual(result, match)

    def test_palindromes_problem_noneinput(self):
        with self.assertRaises(Exception):
            problems.palindromes_problem(None)


if __name__ == '__main__':
    unittest.main()
