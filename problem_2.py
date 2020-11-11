
import os
import sys
from sys import argv
from exceptions import InvalidInput


def find_palindroms_str(input: str):
    if not isinstance(input, str):
        raise InvalidInput("Input must be str")

    isPal = ''
    pals = []

    i = len(input)

    while(i > 0):
        isPal += input[:i]
        if isPal == isPal[::-1]:
            pals.append(isPal)
            input = input[i:]
            i = len(input)
        else:
            i -= 1
        isPal = ''

    return pals


def main():
    if "run_tests" == sys.argv[1]:
        print('Running tests...')
        os.system('python test_{} -v'.format(argv[0]))
    else:
        for arg in sys.argv[1:]:
            print(find_palindroms_str(input=arg))


if __name__ == "__main__":
    main()
