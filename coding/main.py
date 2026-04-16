import datetime as dt
import bday_messages as bday

today = dt.date.today()
next_birthday = dt.date(2026, 7, 17)
my_age = dt.date(2003, 7, 17)

days_away = next_birthday - today
my_age_today = today - my_age

if today == next_birthday:
    print(bday.random_message)
else:
    print(f"My next birthday is {days_away.days} days away!")

print(f"I'm alive {my_age_today.days} days in the Earth.")