def squareRoot(radicant):
    if isinstance(radicant, str):
        return "Trying to use strings in calculator"
    from math import sqrt
    return sqrt(radicant)
