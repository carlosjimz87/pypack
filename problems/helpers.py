
class InvalidArgs(Exception):
    pass


class InvalidInput(Exception):
    pass


def validateStr(input):
    if not isinstance(input, str):
        raise InvalidInput("Input must be str")
    else:
        return input


def validateList(input):
    if not input or not input[0] or not isinstance(input[0], tuple):
        raise InvalidInput(
            "Invalid list of tuples. Correct format is List[Tuple[int,int]]")

    else:
        i, j = input[0]
        if not isinstance(i, int) and not isinstance(j, int):
            raise InvalidInput(
                "Invalid list of tuples. Pairs must be int numbers")

        return input


def parse(inputs):
    try:
        if isinstance(eval(inputs[0]), int):
            return [(int(inputs[i]), int(inputs[i+1])) for i in range(0, len(inputs), 2)]

    except:
        raise InvalidArgs(
            "Type separate numbers for bishop' positions as [x1] [y1] [x2] [y2] - [xN] [yn]. Or type 'run_tests' to run unittests")
