import random

question = input("Question: ")

randomSelection = random.randint(1, 9)

if randomSelection == 1:
    answer = "Yes - definitely."
elif randomSelection == 2:
    answer = "It is decidedly so."
elif randomSelection == 3:
    answer = "Without a doubt."
elif randomSelection == 4:
    answer = "Reply hazy, try again."
elif randomSelection == 5:
    answer = "Ask again later."
elif randomSelection == 6:
    answer = "Better not tell you now."
elif randomSelection == 7:
    answer = "My sources say no."
elif randomSelection == 8:
    answer = "Outlook not so good."
else:
    answer = "Very doubtful."

print("Magic 8-Ball says: " + answer)
