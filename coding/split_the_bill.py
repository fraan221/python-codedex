bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

total = 0

for i in bill:
    total = total + i

my_share = total / 4
print(total)
print("My Share: " + str(my_share))
