from utils_calc import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute
while True:
    operation = input(
        "Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit): ").lower()
    if operation == "exit":
        break
    elif operation == "add":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add(num1, num2)
    elif operation == "subtract":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = sub(num1, num2)
    elif operation == "multiply":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = multiply(num1, num2)
    elif operation == "divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = divide(num1, num2)
    elif operation == "exponent":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = exponent(num1, num2)
    elif operation == "modulo":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = modulo(num1, num2)
    elif operation == "floor_divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = floor_divide(num1, num2)
    elif operation == "absolute":
        num = float(input("Enter the number: "))
        result = absolute(num)
    else:
        print("Invalid option!")
        continue

    print("The result is:", result)