def categorize_age(age: int) -> str:
    if 0 <= age <= 2:
        return "Baby"
    elif 3 <= age <= 12:
        return "Kid"
    elif 13 <= age <= 17:
        return "Teen"
    elif 18 <= age <= 64:
        return "Adult"
    else:
        return "Older Adult"


a: int = int(input("Enter an Age: "))
print(categorize_age(a))
