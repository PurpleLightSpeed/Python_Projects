# Ask the user a bunch of questions
# If they give us the right answer to these questions we'll add +1 to thier score
# At the end we will give then the number of questions they got right
# ie. 5/10 questions, may also give them a percentage

print("Welcome to the Quiz Game!")

playing = input("Would you like to play? (y/n): ").lower()

if playing != "y":
    quit()

print("Let the Games Begin!!! 😁")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PC stand for? ").lower()
if answer == "personal computer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does DNS stand for? ").lower()
if answer == "domain name system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} answers correct!")
print(f"You got {(score / 5) * 100}%.")

