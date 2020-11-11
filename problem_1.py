

def find_bishops_diagonals(bishops):
    if not bishops or not bishops[0]:
        raise Exception("Empty list of bishops")

    import math
    counter = 0
    seen = set()
    for index, (i, j) in enumerate(bishops):
        for (x, y) in bishops[index+1:]:
            diag1 = math.fabs(i-x)
            diag2 = math.fabs(j-y)
            if (diag1 == diag2):
                counter += 1
                if counter == len(bishops)*2:
                    return counter
    return counter
