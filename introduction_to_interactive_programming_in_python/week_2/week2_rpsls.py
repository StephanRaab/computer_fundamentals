# GUI-based version of RPSLS
import simplegui
import random

# Insert your solution for RPSLS here
def computer_random_number():
    computer = random.randrange(0, 5)
    if (computer == 0):
        return 0
    elif (computer == 1):
        return 1
    elif (computer == 2):
        return 2
    elif (computer == 3):
        return 3
    elif (computer == 4):
        return 4

def number_to_choice(number):
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    else:
        return "scissors"

def choice_to_number(choice):
    if(choice == "rock"):
        return 0
    elif(choice == "Spock"):
        return 1
    elif(choice == "paper"):
        return 2
    elif(choice == "lizard"):
        return 3
    else:
        return 4

def rock():
    print("You chose Rock!")
    return "rock"

def paper():
    print "You chose Paper!"
    return "paper"

def scissors():
    print "You chose Scissors!"
    return "scissors"

def lizard():
    print "You chose Lizard!"
    return "lizard"

def spock():
    print "You chose Spock!"
    return "Spock"

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_button("Rock", rock, 100)
frame.add_button("Paper", paper, 100)
frame.add_button("Scissors", scissors, 100)
frame.add_button("Lizard", lizard, 100)
frame.add_button("Spock", spock, 100)

# Start the frame animation
frame.start()
