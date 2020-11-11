import unittest
import problem_1 as p1


class TestProblem1(unittest.TestCase):

    def test_find_bishops_diagonals_output3(self):
        result = p1.find_bishops_diagonals([(0, 0), (2, 2), (1, 1)])
        self.assertEqual(result, 3)

    def test_find_bishops_diagonals_output2(self):
        result = p1.find_bishops_diagonals(
            [(0, 0), (1, 2), (2, 2), (4, 0)])
        self.assertEqual(result, 2)

    def test_find_bishops_diagonals_output10(self):
        result = p1.find_bishops_diagonals(
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
        self.assertEqual(result, 10)

    def test_find_bishops_diagonals_output0(self):
        result = p1.find_bishops_diagonals(
            [(0, 0), (1, 2), (2, 4), (4, 1)])
        self.assertEqual(result, 0)

    def test_find_palindroms_noneinput(self):
        with self.assertRaises(Exception):
            p1.find_bishops_diagonals(None)


if __name__ == '__main__':
    unittest.main()
