from math import log

def logarithm(antilogarithm, base):
    if isinstance(antilogarithm, str) or isinstance(base, str):
        return "Trying to use strings in calculator"
    solution = log(antilogarithm, base)
    return solution

