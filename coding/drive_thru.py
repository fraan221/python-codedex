# MY SOLUTION
items = [
    '🍔 Classic Burger',
    '🍟 Large Fries',
    '🥤 Cola Drink',
    '🍗 Chicken Nuggets',
    '🌭 Hot Dog',
    '🧀 Bacon Cheese Burger',
    '🥗 Caesar Salad',
    '🍦 Vanilla Sundae'
]

def get_item(order):
    return items[order - 1]


def welcome():
    print("Welcome to Franco’s Fast Food Drive-Thru!\n")
    print("Please choose an item by number:")
    for i in items:
        print(i)
    print("\nEnter the number of the item you want to order.")

welcome()

number_order = int(input("\nNumber: "))
if 1 <= number_order <= 8:
    print("Your choice: " + get_item(number_order))
    print("\nThanks! Enjoy the meal.")
else:
    print("Invalid input.")

# IMPROVES WITH AI

items = [
    '🍔 Classic Burger',
    '🍟 Large Fries',
    '🥤 Cola Drink',
    '🍗 Chicken Nuggets',
    '🌭 Hot Dog',
    '🧀 Bacon Cheese Burger',
    '🥗 Caesar Salad',
    '🍦 Vanilla Sundae'
]

def get_item(order):
    return items[order - 1]


def welcome():
    print("Welcome to Franco’s Fast Food Drive-Thru!\n")
    print("Please choose an item by number:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. ", item)
    print("\nEnter the number of the item you want to order.")

welcome()

number_order = int(input("\nNumber: "))
if 1 <= number_order <= len(items):
    print("Your choice: " + get_item(number_order))
    print("\nThanks! Enjoy the meal.")
else:
    print("Invalid input.")