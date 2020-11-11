
import os
import sys
import math
from sys import argv
from typing import List, Tuple
from exceptions import InvalidInput, InvalidArgs


def validate(input):
    if not input or not input[0] or not isinstance(input[0], tuple):
        raise InvalidInput(
            "Invalid list of tuples. Correct format is List[Tuple[int,int]]")

    else:
        i, j = input[0]
        if not isinstance(i, int) and not isinstance(j, int):
            raise InvalidInput(
                "Invalid list of tuples. Pairs must be int numbers")

        return input


def find_bishops_diagonals(bishops: List[Tuple[int, int]]):
    bishops = validate(bishops)

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


def parse(inputs):
    try:
        if isinstance(eval(inputs[0]), int):
            return [(int(inputs[i]), int(inputs[i+1])) for i in range(0, len(inputs), 2)]

    except:
        raise InvalidArgs(
            "Type separate numbers for bishop' positions as [x1] [y1] [x2] [y2] - [xN] [yn]. Or type 'run_tests' to run unittests")


def main():
    if "run_tests" == sys.argv[1]:
        print('Running tests...')
        os.system('python test_{} -v'.format(argv[0]))
    else:
        bishops = parse(sys.argv[1:])
        print(find_bishops_diagonals(bishops=bishops))


if __name__ == "__main__":
    main()
