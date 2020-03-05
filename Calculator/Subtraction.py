def subtraction(minuend, subtrahend):
    if isinstance(minuend, str) or isinstance(subtrahend, str):
        return "Trying to use strings in calculator"
    return float(minuend) - float(subtrahend)
