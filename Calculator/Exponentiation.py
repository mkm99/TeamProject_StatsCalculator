def exponentiation(base, exponent):
    if isinstance(base, str) or isinstance(exponent, str):
        return "Trying to use strings in calculator"
    solution = float(base) ** exponent
    return solution
