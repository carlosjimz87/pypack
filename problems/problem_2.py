import sys
from . import helpers


def palindromes_problem(bigword: str):
    ''' The Palindromes problem method '''

    bigword = helpers.validate_str(bigword)

    isPal = ''
    pals = []

    i = len(bigword)

    while(i > 0):
        isPal += bigword[:i]
        if isPal == isPal[::-1]:
            pals.append(isPal)
            bigword = bigword[i:]
            i = len(bigword)
        else:
            i -= 1
        isPal = ''

    return pals


if __name__ == "__main__":
    bigword = helpers.parse_args(sys.argv, helpers.PROBLEMS.PALINDROMES)
    print(palindromes_problem(bigword=bigword))
