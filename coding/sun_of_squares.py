total = 0

number = int(input("Integer: "))

for i in range(1, number+1):
    total = (i ** 2) + total

print(f"Final result: {total}")