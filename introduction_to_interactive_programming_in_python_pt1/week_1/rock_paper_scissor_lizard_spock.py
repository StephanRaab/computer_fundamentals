# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    else:
        return 4

def number_to_name(number):
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    else:
        return "scissors"

def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print("")
    # print out the message for the player's choice
    print(("Player chooses " + str(player_choice)))
    # convert the player's choice to player_number using name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print(("Computer chooses " + str(comp_choice)))
    # compute difference of comp_number and player_number modulo five
    comp_number = comp_number % 5
    player_number = player_number % 5

    # use if/elif/else to determine winner, print winner message
    if (comp_number == player_number):
        print("Player and Computer tie!")
    elif((player_number == 0) and (comp_number == 1 or comp_number == 2)):
        print("Computer wins!")
    elif((player_number == 1) and (comp_number == 2 or comp_number == 3)):
        print("Computer wins!")
    elif((player_number == 2) and (comp_number == 3 or comp_number == 4)):
        print("Computer wins!")
    elif((player_number == 3) and (comp_number == 4 or comp_number == 0)):
        print("Computer wins!")
    else:
        print("Player wins!")

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")