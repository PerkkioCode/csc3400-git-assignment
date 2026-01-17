

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
<<<<<<< HEAD
        return "Error: cannot divide by zero (b is 0)"
=======
        return "Error: division by zero"
>>>>>>> e0b4033015e7d4f2a08474ee5ec5c67908e4eecc
    return a / b


def power(a,b):
    return a ** b 


def square_root(a):
    if a < 0:
        return "Error: cannot take square root of a negative number"
    return a ** 0.5


if __name__ == "__main__":
    print("Add:", add(5, 3))
    print("Subtract:", subtract(5, 3))
    print("Multiply:", multiply(5, 3))
    print("Divide:", divide(5, 0))
    print("Power:", power(2,3))	
    print("Square Root:", square_root(-9))
