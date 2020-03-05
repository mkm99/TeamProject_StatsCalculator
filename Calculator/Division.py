def division(dividend, divisor):
    try:
        return float(dividend) / float(divisor)

    except ZeroDivisionError:
        return "Cannot divide by 0"
