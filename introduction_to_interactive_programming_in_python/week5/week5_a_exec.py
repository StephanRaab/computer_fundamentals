# Echo mouse click in console

###################################################
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# global variables
WIDTH = 400
HEIGHT = 600

def click(pos):
    print("Mouse click at " + str(pos))

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register handlers
frame.set_mouseclick_handler(click)

print("======================================================")

# Circle clicking problem

###################################################
# Student should enter code below

import math

# define global constants
RADIUS = 20
RED_POS = [50, 100]
GREEN_POS = [150, 100]
BLUE_POS = [250, 100]

# define helper function
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click(pos):
    if dist(RED_POS, pos) <= RADIUS:
        print("Clicked red ball")
    elif dist(GREEN_POS, pos) <= RADIUS:
        print("Clicked green ball")
    elif dist(BLUE_POS, pos) <= RADIUS:
        print("Clicked blue ball")
    else:
        print("You missed the ball")

# define draw
def draw(canvas):
    canvas.draw_circle(RED_POS, RADIUS, 1, "Red", "Red")
    canvas.draw_circle(GREEN_POS, RADIUS, 1, "Green", "Green")
    canvas.draw_circle(BLUE_POS, RADIUS, 1, "Blue", "Blue")

# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

print("======================================================")