import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    return math.sqrt(x)

def log(x):
    if x <= 0:
        return "Error! Logarithm undefined for zero or negative numbers."
    return math.log10(x)

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number is undefined."
    return math.factorial(int(x))

def trig_function(func, x):
    if func == "sin":
        return math.sin(math.radians(x))
    elif func == "cos":
        return math.cos(math.radians(x))
    elif func == "tan":
        return math.tan(math.radians(x))

while True:
    print("\nAdvanced Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Logarithm (log10(x))")
    print("8. Factorial (x!)")
    print("9. Trigonometry (sin, cos, tan)")
    print("10. Exit")

    choice = input("Enter choice (1-10): ")

    if choice == '10':
        print("Exiting... Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        operations = {'1': add, '2': subtract, '3': multiply, '4': divide, '5': power}
        print(f"Result: {operations[choice](num1, num2)}")

    elif choice == '6':
        num = float(input("Enter a number: "))
        print(f"Result: {sqrt(num)}")

    elif choice == '7':
        num = float(input("Enter a number: "))
        print(f"Result: {log(num)}")

    elif choice == '8':
        num = int(input("Enter a number: "))
        print(f"Result: {factorial(num)}")

    elif choice == '9':
        func = input("Enter function (sin/cos/tan): ").strip().lower()
        num = float(input("Enter angle in degrees: "))
        print(f"Result: {trig_function(func, num)}")

    else:
        print("Invalid input! Please try again.")
