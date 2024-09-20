import random

tries = 0
guess = 0
correctNumber = random.randint(0, 99)

print(".: THE HIGHER OR LOWER GAME :.")
print("---------------------------")
print("Welcome to The Higher Lower Game.\n I will randomize a number between 0 and 99. Can you guess it?")
print("---------------------------")
#print("correct numb", correctNumber)

guess = int(input("your guess: \n>"))

while True:
    tries += 1
    if guess == correctNumber:
        print("---------------------------")
        print(f"{guess} is correct!\nIt took you {tries} guesses.\nGood job!")
        exit()
    else:
        if guess < correctNumber:
            print("HIGHER!")
        else:
            print("LOWER!")
    guess = int(input("Try again: \n>"))
    
