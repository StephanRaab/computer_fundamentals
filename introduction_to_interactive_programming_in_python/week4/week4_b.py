# Key board debugging - debug and fix the code below

import simplegui

message = "Welcome!"

# Handler for keydown
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["up"]:
        message = "Up arrow"
    elif key == simplegui.KEY_MAP["down"]:
        message = "Down arrow"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# Start the frame animation
frame.start()

print "========================================"

# Ball radius control - version 1

import simplegui

WIDTH = 300
HEIGHT = 200
ball_radius = 50
BALL_RADIUS_INC = 3

# Handler for keydown
def keydown(key):
    global ball_radius
    if key == simplegui.KEY_MAP["up"]:
        ball_radius += 10
    elif key == simplegui.KEY_MAP["down"]:
        ball_radius -= 10

# Handler to draw on canvas
def draw(canvas):
    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

print "========================================"

# Space bar status

import simplegui

message = "Space bar up"

# Handlers for keydown and keyup
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar down"

def keyup(key):
    global message
    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar up"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [25, 112], 42, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

print "========================================"

# Ball radius control - version 2

import simplegui

WIDTH = 300
HEIGHT = 200
ball_radius = 10
ball_growth = 0
BALL_GROWTH_INC = .2


# Handlers for keydown and keyup
def keydown(key):
    global ball_growth
    if key == simplegui.KEY_MAP["up"]:
        ball_growth = BALL_GROWTH_INC


def keyup(key):
    global ball_growth
    if key == simplegui.KEY_MAP["up"]:
        ball_growth = 0


# Handler to draw on canvas
def draw(canvas):
    global ball_radius
    ball_radius += ball_growth

    # note that CodeSkulptor throws an error if radius is not positive
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], ball_radius, 1, "White", "White")


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()