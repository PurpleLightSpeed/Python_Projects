from random import randint as ran
print("Welcome to the Number Guessing Game!")
number = ran(1,100)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        if guess < number:
         print("Too low! Try again.")

        elif guess > number:
         print("Too high! Try again.")

        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")
