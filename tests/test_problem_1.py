import unittest
from .context import problems


class TestProblem1(unittest.TestCase):

    def test_bishops_problem_output3(self):
        result = problems.bishops_problem([(0, 0), (2, 2), (1, 1)])
        self.assertEqual(result, 3)

    def test_bishops_problem_output2(self):
        result = problems.bishops_problem(
            [(0, 0), (1, 2), (2, 2), (4, 0)])
        self.assertEqual(result, 2)

    def test_bishops_problem_output10(self):
        result = problems.bishops_problem(
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
        self.assertEqual(result, 10)

    def test_bishops_problem_output0(self):
        result = problems.bishops_problem(
            [(0, 0), (1, 2), (2, 4), (4, 1)])
        self.assertEqual(result, 0)

    def test_find_palindroms_noneinput(self):
        with self.assertRaises(Exception):
            problems.bishops_problem(None)


if __name__ == '__main__':
    unittest.main()
