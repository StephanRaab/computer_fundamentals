# "Guess the number" mini-project
# input will come from buttons and an input field
import math, random, simplegui

# helper function to start and restart the game
def new_game():
    """
    initialize global variables used in your code here
    """
    global secret_number
    secret_number = random.randrange(0, 100)
    global guess_left
    guess_left = 7
    return(secret_number, guess_left)

def range100():
    """
    button that changes the range to [0,100) and starts a new game
    """
    global secret_number
    secret_number = random.randrange(0, 100)
    global guess_left
    guess_left = 7
    print("You're playing from 0 - 100!")

def range1000():
    """
    button that changes the range to [0,1000) and starts a new game
    """
    global secret_number
    secret_number = random.randrange(0, 1000)
    global guess_left
    guess_left = 10
    print("You're playing from 0 - 1000!")

def input_guess(guess):
    """
    main game logic goes here
    """
    global guess_left
    guess_left -= 1
    print("")
    print("Guess was " + str(guess))
    if(int(guess) < secret_number):
        print("Higher")
        print("You have " + str(guess_left) + " left!")
    elif(int(guess) > secret_number):
        print("Lower")
        print("You have " + str(guess_left) + " left!")
    else:
        print("Correct")
        print("You had " + str(guess_left) + " left!")

# create frame
frame = simplegui.create_frame("Guess The Number", 300, 300)
frame.add_button("Range is [0,100)", range100, 150)
frame.add_button("Range is [0,1000)", range1000, 150)
frame.add_input("Input your guess", input_guess, 150)

# register event handlers for control elements and start frame
frame.start()

# call new_game
new_game()