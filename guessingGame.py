import random

number = random.randint(1, 9)
lifes = 5

print("Guess the number between 1 and 9:")
while lifes > 0:
    userInput = int(input("Enter your guess: "))
    if userInput != number:
        lifes -= 1
        if userInput > number:
            print(f"Try guessing a number less than {userInput}")
        else:
            print(f"Try guessing a number more than {userInput}")
    else:
        print("Your guess was correct!")
        break

if lifes == 0:
    print(f"You lose! The number was {number}")
