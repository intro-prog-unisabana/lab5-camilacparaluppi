from utils import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute
while True:
    operacion = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):").lower()
    if operacion not in ["add","subtract","multiply","divide","exponent","modulo","floor_divide","absolute"]:
        print("Invalid option!")
        continue
    elif operacion == "exit":
        break
    elif operacion == "absolute":
        num = float(input("Enter the number:"))
        result = absolute(num)
        print(f"The result is: {result}")
    else:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
    
    if operacion == "add":
        result = add(num1, num2)
    elif operacion == "subtract":
        result = sub(num1, num2)
    elif operacion == "multiply":
        result = multiply(num1, num2)
    elif operacion == "divide":
        result = divide(num1, num2)
    elif operacion == "exponent":
        result = exponent(num1, num2)
    elif operacion == "modulo":
        result = modulo(num1, num2)
    elif operacion == "floor_divide":
        result = floor_divide(num1, num2)
    print(f"The result is: {result}")