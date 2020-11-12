
import os
import sys
import math
from sys import argv
from . import helpers
from typing import List, Tuple


def find_bishops_diagonals(bishops: List[Tuple[int, int]]):
    bishops = helpers.validateList(bishops)

    counter = 0
    for index, (i, j) in enumerate(bishops):
        for (x, y) in bishops[index+1:]:
            diag1 = math.fabs(i-x)
            diag2 = math.fabs(j-y)
            if (diag1 == diag2):
                counter += 1
                if counter == len(bishops)*2:
                    return counter
    return counter


def main():
    if "run_tests" == sys.argv[1]:
        print('Running tests...')
        os.system('python test_{} -v'.format(argv[0]))
    else:
        bishops = helpers.parse(sys.argv[1:])
        print(find_bishops_diagonals(bishops=bishops))


if __name__ == "__main__":
    main()
