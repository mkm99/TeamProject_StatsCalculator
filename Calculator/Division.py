def division(dividend, divisor):
    if isinstance(dividend, str) or isinstance(divisor, str):
        return "Trying to use strings in calculator"
    try:
        return float(dividend) / float(divisor)

    except ZeroDivisionError:
        return "Cannot divide by 0"
