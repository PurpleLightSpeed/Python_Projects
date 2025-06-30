from random import randint as ran
print("Welcome to the Number Guessing Game!")
number = ran(1,100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    elif guess == number:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break
    else:
        print("Please enter a valid number.")