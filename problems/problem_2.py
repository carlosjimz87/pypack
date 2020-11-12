
import os
import sys
from sys import argv
from . import helpers


def palindromes_problem(input: str):
    input = helpers.validateStr(input)

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
            print(palindromes_problem(input=arg))


if __name__ == "__main__":
    main()
