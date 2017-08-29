# Add "Hello" and "Goodbye" buttons

import simplegui

# Handlers for buttons
def print_hello():
    print("Hello")

def print_goodbye():
    print("Goodbye")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)

# Start the frame animation
frame.start()

# Test
print_hello()
print_hello()
print_goodbye()
print_hello()
print_goodbye()

print("################################################################")

# Register three buttons
import simplegui

# Handlers for buttons
def set_red():
    global color
    color = "red"

def set_blue():
    global color
    color = "blue"

def print_color():
    print(color)

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)

# Create frame buttons
frame.add_button("red", set_red, 100)
frame.add_button("blue", set_blue, 100)
frame.add_button("print color", print_color, 100)

# Start the frame animation
frame.start()

# Test
set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

print("################################################################")

# GUI with buttons to manipulate global variable count
import simplegui

# Define event handlers for four buttons
def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def reset():
    global count
    count = 0

def print_count():
    global count
    print(count)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Count Operations", 300, 300)

frame.add_button("Increase", increment, 100)
frame.add_button("Decrease", decrement, 100)
frame.add_button("Reset Count", reset, 100)
frame.add_button("Print Count", print_count, 100)

# Start the frame animation
frame.start()

# Test
reset()
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()


print("################################################################")

# Echo an input field
import simplegui

# Handlers for input field\
def get_input(input):
    print(input)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)
frame.add_input("Input Text", get_input, 100)

# Start the frame animation
frame.start()

# Test
get_input("First test input")
get_input("Second test input")
get_input("Third test input")

print("################################################################")

# Convert input text into Pig Latin
import simplegui

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    first_letter = word[0]
    rest_of_word = word[1 : ]
    if(first_letter == 'a' or
       first_letter == 'e' or
       first_letter == 'u' or
       first_letter == 'i' or
       first_letter == 'o'):
        return(word + "way")
    else:
        return(rest_of_word + first_letter + "ay")

# Handler for input field
def get_input(word):
    print(pig_latin(word))

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Input Regular English", get_input, 100)

# Start the frame animation
frame.start()

# Test
get_input("pig")
get_input("owl")
get_input("tree")

print("################################################################")

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