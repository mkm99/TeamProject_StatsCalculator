def multiply(multiplier, multiplicant):
    if isinstance(multiplier, str) or isinstance(multiplicant, str):
        return "Trying to use strings in calculator"
    return float(multiplier) * float(multiplicant)