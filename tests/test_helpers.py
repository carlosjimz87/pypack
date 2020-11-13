from problems import helpers
from .context import problems
from contextlib import contextmanager
import pytest


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    "input,expectation",
    [
        ("string", does_not_raise()),
        ("", does_not_raise()),
        (0, pytest.raises(problems.helpers.InvalidArgs)),
        (None, pytest.raises(problems.helpers.InvalidArgs)),
    ],
)
def test_validate_str(input, expectation):
    """Test validation of the string inputs."""
    with expectation:
        problems.helpers.validate_str(input)


@pytest.mark.parametrize(
    "input,expectation",
    [
        ([(1, 1)], does_not_raise()),
        ([("1", "1")], pytest.raises(problems.helpers.InvalidArgs)),
        ([(None, None)], pytest.raises(problems.helpers.InvalidArgs)),
        ([], pytest.raises(problems.helpers.InvalidArgs)),
        (0, pytest.raises(problems.helpers.InvalidArgs)),
        ("", pytest.raises(problems.helpers.InvalidArgs)),
        (None, pytest.raises(problems.helpers.InvalidArgs)),
    ],
)
def test_validate_list_of_tuples(input, expectation):
    """Test the validation of the list of tuples."""
    with expectation:
        problems.helpers.validate_list_of_tuples(input)


@pytest.mark.parametrize(
    "input,expectation",
    [

        (["1", "1"], [(1, 1)]),
        (["1", "1", "2", "2"], [(1, 1), (2, 2)]),
        (None, problems.helpers.MENU),
    ],
)
def test_parse_list_of_tuples(input, expectation):
    """Test the parsing of the list of tuples."""
    assert(problems.helpers.parse_list_of_tuples(input) == expectation)


@pytest.mark.parametrize(
    "input,expectation",
    [

        (["/Pyfolder/folder/problem_1.py", "run_tests"], None),
        (["/Pyfolder/folder/problem_1.py", "run_tests abc"], None),
        (["/Pyfolder/folder/problem_1.py", "run_tests 2 2 2"], None),
        (["/Pyfolder/folder/problem_1.py", "2 2 run_tests"], None),
        (["/Pyfolder/folder/problem_1.py", ""], problems.helpers.MENU),
    ],
)
def test_parse_args_run_tests_problem1(input, expectation):
    """Test the parsing of main args for cases related with run_tests."""
    assert(problems.helpers.parse_args(
        input, helpers.PROBLEMS.BISHOPS) == expectation)


@pytest.mark.parametrize(
    "input,expectation",
    [
        (["/Pyfolder/folder/problem_1.py", "1 1"], [(1, 1)]),
        (["/Pyfolder/folder/problem_1.py", "1 1 2 2"], [(1, 1), (2, 2)]),
        (["/Pyfolder/folder/problem_1.py", "2 2 3 3"], [(2, 2), (3, 3)]),
        (["/Pyfolder/folder/problem_1.py", ""], problems.helpers.MENU),
    ],
)
def test_parse_args_problem1(input, expectation):
    """Test the parsing of main args for problem1."""
    assert(problems.helpers.parse_args(
        input, helpers.PROBLEMS.BISHOPS) == expectation)


@pytest.mark.parametrize(
    "input,expectation",
    [
        (["/Pyfolder/folder/problem_2.py", "abc"], "abc"),
        (["/Pyfolder/folder/problem_2.py", "racecarannakayak"], "racecarannakayak"),
        (["/Pyfolder/folder/problem_2.py", ""], problems.helpers.MENU),
    ],
)
def test_parse_args_problem2(input, expectation):
    """Test the parsing of main args for problem2."""
    assert(problems.helpers.parse_args(
        input, helpers.PROBLEMS.PALINDROMES) == expectation)
