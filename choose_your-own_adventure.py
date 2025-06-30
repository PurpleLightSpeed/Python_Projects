def not_valid_option():
    print("Not a Valid option. Please try again")

def chapter_3AB():
    if answer == "3A":
        print("You gather evidence and broadcast it across the city, igniting a wave of rebellion.")
        print("Ending 1: The city rises, and you become a symbol of hope.")
    elif answer == "3B":
        print("You infiltrate the corporation, disabling the mind-control project but becoming a fugitive hunted by mercenaries.")
        print("Ending 2: A lone rebel fighting for freedom in the shadows.")
    else:
        not_valid_option()

def chapter_3CD():
    if answer == "3C":
        print("Using your powers, you disable weapons and flee into the neon-lit maze of Night City.")
        print("Ending 3: Survivor in a city that never sleeps.")
    elif answer == "3D":
        print("Your confrontation earns you respect and a new gang’s loyalty, but also new enemies.")
        print("Ending 4: Rise to power in the city’s underworld.")
    else:
        not_valid_option()

def chapter_3EF():
    if answer == "3E":
        print("Under Cipher’s guidance, your power grows strong and controlled.")
        print("Ending 5: Protector of Night City, balancing light and shadow.")
    elif answer == "3F":
        print("Without training, your power becomes volatile, leading to unpredictable consequences.")
        print("Ending 6: A wild force of change — for better or worse.")
    else:
        not_valid_option()

def chapter_3GH():
    if answer == "3G":
        print("The figure leads you to an ancient underground network that holds the key to mastering your power.")
        print("Ending 7: Discoverer of forgotten knowledge and new beginnings.")
    elif answer == "3H":
        print("Your solitary path reveals hidden allies and enemies alike.")
        print("Ending 8: A mysterious force shaping the fate of Night City from the shadows.")
    else:
        not_valid_option() 

name = input("What's your name? ")
print(f"Welcome {name} to the adventure")

print("You feel a sudden rush of energy coursing through your veins. Your vision sharpens, and your senses heighten. The device pulses softly in your hand.")
print("1A: Attempt to harness this power and experiment with its capabilities.")
print("1B: Hide the device and seek the help of a trusted hacker friend.")
answer = input("(1A or 1B): ").upper()

if answer == "1A":
    print("You focus your mind and try to control the energy inside you. Suddenly, a holographic interface appears before your eyes, revealing encrypted data about Night City's darkest secrets.")
    print("2A: Dive into the data and uncover the hidden truths.")
    print("2B: Use your newfound power to defend yourself from suspicious gang members who notice your glow.")
    answer = input("(2A or 2B): ").upper()

    if answer == "2A":
        print("The data reveals a conspiracy: a powerful corporation plans to enslave the city's population using a mind-control implant.")
        print("3A: Expose the corporation to the public.")
        print("3B: Infiltrate the corporation to sabotage their plans from within.")
        answer = input("(3A or 3B): ").upper()
        chapter_3AB()

    elif answer == "2B":
        print("The gang members approach aggressively. Your power flares, and you can manipulate electronic devices around you.")
        print("3C: Use your power to disable their weapons and escape.")
        print("3D: Confront them head-on, showing your strength to gain respect.")
        answer = input("(3C or 3D): ").upper()
        chapter_3CD()
    else:
        not_valid_option()
elif answer == "1B":
    print("You rush to your hacker friend, a cunning and resourceful figure known as Cipher. Cipher's eyes widen as you reveal the device.")
    print("2C: Trust Cipher to decode the device and guide you.")
    print("2D: Keep the device secret and prepare to explore the city alone.")
    answer = input("(2C or 2D): ").upper()

    if answer == "2C":
        print("Cipher decodes the device and warns you: the power you hold is unstable but can be controlled with training.")
        print("3E: Begin training under Cipher's mentorship.")
        print("3F: Reject training and rely on instinct to control the power.")
        answer = input("(3E or 3F): ").upper()
        chapter_3EF()

    elif answer == "2D":
        print("You come across a mysterious figure offering information about the device.")
        print("3G: Accept the offer and follow the figure.")
        print("3H: Decline and continue your own investigation.")
        answer = input("(3G or 3H): ").upper()
        chapter_3GH()

    else:
        not_valid_option()
else:
    not_valid_option()

