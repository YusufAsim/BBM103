import random
number = random.randint(1, 20)
guess = int(input("Guess the random number between 1 and 20\nenter your prediction:"))

while guess != number:
    if guess > number:
        print(" decrease your number")
        guess = int(input("Guess the random number between 1 and 20\nenter your prediction:"))
    else:
        print("increase your number")
        guess = int(input("Guess the random number between 1 and 20\nenter your prediction:"))
