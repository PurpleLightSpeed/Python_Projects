import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {
    ROCK: "🪨",
    SCISSORS: "✂️",
    PAPER: "📜"
}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        player_choice = input("rock, paper, or scissors? (r/p/s): ").lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Invalid Choice")

def display_choices(player_choice, computer_choice):
    print(f"You choose {emojis[player_choice]}")
    print(f"Computer choose {emojis[computer_choice]}")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("It's a Tie!")
    elif(
        (player_choice == ROCK and computer_choice == SCISSORS) or
        (player_choice == PAPER and computer_choice == ROCK) or
        (player_choice == SCISSORS and computer_choice == PAPER)):
        print("You Win!")
    else:
        print("You Lose!")

def play_game():
    while True:
        player_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(player_choice, computer_choice)

        determine_winner(player_choice, computer_choice)
            
        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            break

play_game()