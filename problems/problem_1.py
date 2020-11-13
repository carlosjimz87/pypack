
import math
import sys
from . import helpers
from typing import List, Tuple


def bishops_problem(bishops: List[Tuple[int, int]]):
    ''' The Bishops problem method '''
    bishops = helpers.validate_list_of_tuples(bishops)
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


if __name__ == "__main__":
    bishopsList = helpers.parse_args(sys.argv, helpers.PROBLEMS.BISHOPS)
    print(bishops_problem(bishopsList=bishopsList))
