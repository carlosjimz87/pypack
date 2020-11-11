

def find_bishops_diagonals(bishops):
    if not bishops or not bishops[0]:
        return []

    import math
    counter = 0

    for index, (i, j) in enumerate(bishops):
        for (x, y) in bishops[index+1:]:
            if math.fabs(i-x) == math.fabs(j-y):
                counter += 1
    return counter


bishops = [(0, 0), (1, 2), (2, 2), (4, 0)]
print(find_bishops_diagonals(bishops))
