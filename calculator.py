
def add(a, b):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Error: inputs must be numbers"
    return a + b


def subtract(a, b):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Error: inputs must be numbers"
    return a - b


def multiply(a, b):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Error: inputs must be numbers"
    return a * b


def divide(a, b):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Error: inputs must be numbers"
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def power(a, b):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Error: inputs must be numbers"
    return a ** b


def square_root(a):
    if type(a) != int and type(a) != float:
        return "Error: input must be a number"
    if a < 0:
        return "Error: cannot take square root of a negative number"
    return a ** 0.5
