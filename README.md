# Problems

This is a python package that solves the Palindromes and Bishops problems.

## Installation

Run the following to install:

```
python -m pip install --upgrade pip
pip install git+https://github.com/carlosjimz87/pyrepo.git@restructured --upgrade
```

## Usage

```
python import problems

# Bishops problem
problems.bishops_problem([(0, 0), (2, 2), (1, 1)])

# Palindromes problem
problems.palindromes_problem("racecarannakayak")
```

# Development & Test

To install the problems, along with the tools you need to develop and run tests, run the following in your virtualenv:

```
pip install -e .[dev] && pytest -v
```

Thanks!
