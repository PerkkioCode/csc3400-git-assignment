
import calculator

def test(name, result, expected):
    if result == expected:
        print(name + ": PASS")
    else:
        print(name + ": FAIL")
        print(" expected:", expected)
        print(" got:     ", result)

test("Add", calculator.add(2, 3), 5)
test("Subtract", calculator.subtract(10, 4), 6)
test("Multiply", calculator.multiply(3, 5), 15)
test("Divide", calculator.divide(8, 2), 4)
test("Power", calculator.power(2, 3), 8)
test("Square Root", calculator.square_root(9), 3)

test("Divide by zero", calculator.divide(5, 0), "Error: cannot divide by zero")
test("Negative square root", calculator.square_root(-4),
     "Error: cannot take square root of a negative number")
test("Invalid input", calculator.add("abc", 2),
     "Error: inputs must be numbers")
