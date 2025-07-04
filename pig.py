# multiplayer game
# everyone gets to role a die
# when you role a die you get a number thats added to your total score
# you can role as many times as you want until you end your turn
# if you role a one you lose all your points in that turn and its moved to the next player
# first player to 50 or any number set wins

import random

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    
    for player_id in range(players):
        print(f"\nPlayer number {player_id + 1} turn has just started!")
        print(f"Your total score is: {player_scores[player_id]}\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ").lower()
            if should_roll != "y":
                break
            
            value = roll()
            
            if value == 1:
                print(f"You rolled a: {value}! Turn over!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
            
            print(f"Your score is: {current_score}!")
        
        player_scores[player_id] += current_score
        print(f"Your total score is: {player_scores[player_id]}")
max_score = max(player_scores)
winning_id = player_scores.index(max_score)
print(f"\nPlayer number {winning_id + 1} is the winner with a score of: {max_score}\n")