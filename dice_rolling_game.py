import random

# Created a while loop to keep the game running until the user decides to stop
while True:
    #Created an input with the question and placed it inside a variable
    #Used .lower() to turn the input into lowercase
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        #Generate two random numbers between 1 and 6 to simulate dice rolls
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thanks for playing")
        #break the loop to end the game
        break
    else:
        print("Invalid Coice!")