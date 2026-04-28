def calculator(num1: int, num2: int, operation: str):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 > 0 else "Division by Zero Detected"
    else:
        return "Invalid Operation."


n1: int = int(input("Enter the first number: "))
n2: int = int(input("Enter the second number: "))
o: str = input("Enter the operation('+', '-', '*' or '/'): ")

print(calculator(n1, n2, o))
