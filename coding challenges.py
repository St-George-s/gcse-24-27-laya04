import random
number = random.randint(1,50)

userGuess = ("Guess the number:")
if userGuess > number:
    print("Too high!")
if userGuess < number:
    print("Too high!")