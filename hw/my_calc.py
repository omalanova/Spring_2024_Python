#my_calc.py
def add(x, y):
    return x + y


def remain(x, y):
    return x % y


def subtract(x, y):
    return x - y


def prod(x, y):
    return x * y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Can't divide by zero"