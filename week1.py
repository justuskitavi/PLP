# Simple calculator program

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation you want to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

# Perform the operation
if operation == "1":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "2":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "3":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter 1, 2, 3, or 4.")
