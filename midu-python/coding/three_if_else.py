def is_leap(year: int) -> str:
    leap: bool = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    if leap:
        return f"{year} is Leap."
    else:
        return f"{year} is not Leap."


y: int = int(input("Enter a year: "))
print(is_leap(y))
