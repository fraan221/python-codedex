import random

hp = 100
bug_fixed = False
answer = 0

print("Checkout Project - Issue in the Server")
print("------------------------------------------")

print("\nOptions")
print("1. Reset server")
print("2. Debug code")
print("3. Ask for help in Stack Overflow")

while hp > 0 and bug_fixed == False:
    answer = int(input("\nChoose one option: "))
    num_ran = random.randint(1, 100)
    if answer == 1:
        bug_fixed = True
        hp = hp - 10
        print("\nServer fixed 😃")
    elif answer == 2:
        if num_ran == 10:
            bug_fixed = True
            hp = hp - 35
            print("\nServer fixed 😃🤕")
        else:
            bug_fixed = False
            print("\nI cannot find the Issue 😭")
            hp = hp - num_ran
    elif answer == 3:
        bug_fixed = True
        hp = hp - 50
        print("\nI'm finding some fixes in Stack Overflow...")
        print("Server fixed 😃🤕😭")
    else:
        print("\nWrong input.")
    print(f"Final health: {hp}")


if hp <= 0 or bug_fixed == False:
    print("I cannot fix the Issue 😭")
elif answer == 1:
    print("I fixed the Issue by Resetting the Server.")
elif answer == 2:
    print("I fixed the Issue by Debugging Code.")
elif answer == 3:
    print("I fixed the Issue by Asking for Help in Stack Overflow.")