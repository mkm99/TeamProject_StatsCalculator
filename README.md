[![Build Status](https://travis-ci.com/mkm99/TeamProject_StatsCalculator.svg?branch=master)](https://travis-ci.com/mkm99/TeamProject_StatsCalculator)

# TeamProject_StatsCalculator
**Team Members**
- Mary Machado
- Mario Suarez

<br>

This projects, we built an statistics calculator which have the following functions:
[Calculator Functions](/Overview.md)

To make sure the calculator works correctly, test cases were added using **Unittest** framework.
Four different test files were created
- [Tests for Calculator](/Tests/test_calculator.py)
- [Tests for Creation of random numbers](/Tests/test_random.py)
- [Tests for Statistics Functions](/Tests/test_statistics_functions.py)
- [Tests for Population Sampling](/Tests/test_population_sampling.py)

In the *Test for Statistics Functions* there are functions that checks the behavior of the Calculator's Statistics Functions.
In this file, each function is checked twice, one by importing the file and the class where the function exists, and the
second function uses the built-in functions that exists in libraries such as **Statistics** and **Numpy** both test functions
utilize the same data, and both test functions **must produce the same results**, this way we make sure that the calculator is
behaving as is supposed to.

 
