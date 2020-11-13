
import os
from enum import Enum
import ntpath
ntpath.basename("a/b/c")


class PROBLEMS(Enum):
    BISHOPS = 1
    PALINDROMES = 2


MENU = (
    '''
    !!! Invalid Arguments !!!  \n
     - For Bishop problem:: Type separated positions as [x1] [y1] [x2] [y2] ... [xN] [yN].\n
     - For Palindrome problem :: Type any word strings.\n
     - Or type 'run_tests' as first arg to run all tests
     ''')


class InvalidArgs(Exception):
    def __init__(self, message="Invalid Arguments. Type numbers with this format: x1 y1 x2 y2 [...] xN yN"):
        self.message = message
        super().__init__(self.message)


def validate_str(input):
    ''' This method validate that input of the Palindromes problem (problem2) is correct '''
    if not isinstance(input, str):
        raise InvalidArgs(message="Invalid Arguments. Type any word strings")
    else:
        return input


def validate_list_of_tuples(input):
    ''' This method validate that input of the Bishops problem (problem1) is correct '''

    if not input or not input[0] or not isinstance(input[0], tuple):
        raise InvalidArgs()

    else:
        i, j = input[0]
        if not isinstance(i, int) and not isinstance(j, int):
            raise InvalidArgs()

        return input


def parse_list_of_tuples(input):
    ''' This method parse the main arguments using the eval built-in function 
    and returns a list of tuples of numbers to feed the Bishops problem (problem1) '''

    try:
        if isinstance(eval(input[0]), int):
            return [(int(input[i]), int(input[i+1])) for i in range(0, len(input), 2)]
    except:
        return MENU


def path_filename(path):
    ''' This method crops the filename of a path '''
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def parse_args(argv, problem_num):
    ''' This method parse the main arguments and returns the corresponding 
        inputs for each problem or execute the tests if the run_tests arg 
        is in the first position '''
    if len(argv) <= 1 or len(argv[1]) == 0:
        return MENU

    if "run_tests" in argv[1]:
        filename = "test_"+path_filename(argv[0])
        print(f'Running tests of {filename}')
        os.system(f'pytest {filename} ')

    else:
        if problem_num == PROBLEMS.BISHOPS:
            return parse_list_of_tuples(argv[1].split(" "))
        if problem_num == PROBLEMS.PALINDROMES:
            return argv[1]
        else:
            return MENU
