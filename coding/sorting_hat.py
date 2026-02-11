gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print("\nWelcome to the Sorting Hat Quiz!")
print("--------------------------------\n")

# Q1
print("Q1) Do you like Dawn or Dusk? ")
print("  1) Dawn")
print("  2) Dusk")
answerQ1 = int(input("Choose: "))

if answerQ1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answerQ1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

# Q2
print("\nQ2) When I’m dead, I want people to remember me as:")
print("  1) The Good")
print("  2) The Great")
print("  3) The Wise")
print("  4) The Bold")
answerQ2 = int(input("Choose: "))

if answerQ2 == 1:
    hufflepuff += 2
elif answerQ2 == 2:
    slytherin += 2
elif answerQ2 == 3:
    ravenclaw += 2
elif answerQ2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

# Q3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("  1) The violin")
print("  2) The trumpet")
print("  3) The piano")
print("  4) The drum")
answerQ3 = int(input("Choose: "))

if answerQ3 == 1:
    slytherin += 4
elif answerQ3 == 2:
    hufflepuff += 4
elif answerQ3 == 3:
    ravenclaw += 4
elif answerQ3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")

print("\nFINAL SCORE: ")
print("Gryffindor: " + str(gryffindor))
print("Hufflepuff: " + str(hufflepuff))
print("Ravenclaw: " + str(ravenclaw))
print("Slytherin: " + str(slytherin))

print("\nMOST POINTS:")
if gryffindor >= hufflepuff and gryffindor >= ravenclaw and gryffindor >= slytherin:
    print("Gryffindor")
elif hufflepuff >= ravenclaw and hufflepuff >= slytherin:
    print("Hufflepuff")
elif ravenclaw >= slytherin:
    print("Ravenclaw")
else:
    print("Slytherin")
