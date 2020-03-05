def addition(augend, addend):
    if isinstance(augend, str) or isinstance(addend, str):
        return "Trying to use strings in calculator"
    solution = float(augend) + float(addend)
    return solution

