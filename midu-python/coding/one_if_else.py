def greater_than_or_equal(num1: int, num2: int):
    if num1 > num2:
        return f"{num1} is greater."
    elif num2 > num1:
        return f"{num2} is greater."
    else:
        return f"{num1} and {num2} are equal."


n1: int = int(input("Enter first number: "))
n2: int = int(input("Enter second number: "))

print(greater_than_or_equal(n1, n2))
