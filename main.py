

import calculator

def show_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")


while True:
    show_menu()
    choice = input("Choose an option (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice == "6":
        num = float(input("Enter a number: "))
        result = calculator.square_root(num)
        print("Result:", result)
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = calculator.add(num1, num2)
    elif choice == "2":
        result = calculator.subtract(num1, num2)
    elif choice == "3":
        result = calculator.multiply(num1, num2)
    elif choice == "4":
        result = calculator.divide(num1, num2)
    elif choice == "5":
        result = calculator.power(num1, num2)
    else:
        print("Invalid choice")
        continue

    print("Result:", result)
