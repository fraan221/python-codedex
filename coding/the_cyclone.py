height_requirement = int(input("Height: "))
credit_requirement = int(input("Credits: "))

if height_requirement >= 137 and credit_requirement >= 10:
    print("Enjoy the ride!")
elif credit_requirement >= 10 and height_requirement < 137:
    print("You are not tall enough to ride.")
elif height_requirement >= 137 and credit_requirement < 10:
    print("You don't have enough credits.")
else:
    print("You did not met either requirement.")
