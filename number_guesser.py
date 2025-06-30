# Generate a random number
# Track how many times it takes the user to gues the number

import random


try:

    top_of_range = int(input("Type a number: "))
    random_number = random.randint(1, top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()

    guesses = 0

    while True:
        guesses += 1
        user_guess = int(input("Make a guess: "))
        if user_guess == random_number:
            print("You've guessed the number")
            break
        elif user_guess < random_number:
            print("The right number is higher")
        elif user_guess > random_number:
            print("the number is lower")
        else:
            continue

    print(f"You got it in {guesses} trys!")

except ValueError:
    print("Please type a number next time.")
    


