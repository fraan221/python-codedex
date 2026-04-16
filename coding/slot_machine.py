import random

# VERSION 1
# symbols = ["🍒", "🍇", "🍉", "7️⃣"]

# results = random.choices(symbols, k=3)

# print(f" {results[0]}  |  {results[1]}  |  {results[2]}")

# if (
#     results[0] == symbols[-1]
#     and results[1] == symbols[-1]
#     and results[2] == symbols[-1]
# ):
#     print("Jackpot! 💰")
# else:
#     print("Thanks for playing!")


# VERSION 2

symbols = ["🍒", "🍇", "🍉", "7️⃣"]


def play():
    results = random.choices(symbols, k=3)

    print(f"\n {results[0]}  |  {results[1]}  |  {results[2]}")
    win = (
        results[0] == symbols[-1]
        and results[1] == symbols[-1]
        and results[2] == symbols[-1]
    )

    if win:
        print("Jackpot! 💰\n")
    else:
        print("Thanks for playing!\n")


play()
answer = input("Keep playing? (Y/N) ").upper()

while answer.upper() != "N":
    if answer == "Y":
        play()
    else:
        print("Invalid. Enter Y/N")
    answer = input("Keep playing? (Y/N) ").upper()


# VERSION CODEDEX

# import random

# symbols = ["🍒", "🍇", "🍉", "7️⃣"]


# def play():

#     for i in range(1, 51):
#         results = random.choices(symbols, k=3)
#         print(f"{results[0]} | {results[1]} | {results[2]}")
#         win = results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣"

#         if win:
#             print("Jackpot!!! 💰")
#             break
#         else:
#             results = random.choices(symbols, k=3)


# answer = ""
# while answer.upper() != "N":
#     play()
#     answer = input("Keep playing? (Y/N) ")

# print("Thanks for playing!")
