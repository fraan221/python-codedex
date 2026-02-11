a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

x_1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
x_2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

print(x_1)
print(x_2)
