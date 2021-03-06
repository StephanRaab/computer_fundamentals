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

# Day to number problem
###################################################

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def day_to_number(day):
    return day_list.index(day)


###################################################
# Test data

print day_to_number("Sunday")
print day_to_number("Monday")
print day_to_number("Tuesday")
print day_to_number("Wednesday")
print day_to_number("Thursday")
print day_to_number("Friday")
print day_to_number("Saturday")

###################################################
# Sample output

# 0
# 1
# 2
# 3
# 4
# 5
# 6

print("======================================================")

# String list joining problem
###################################################

def string_list_join(string_list):
    string = ""
    for i in range(len(string_list)):
        string += string_list[i]
    return string


###################################################
# Test data

print(string_list_join([]))
print(string_list_join(["pig", "dog"]))
print(string_list_join(["spam", " and ", "eggs"]))
print(string_list_join(["a", "b", "c", "d"]))


###################################################
# Output

#
#pigdog
#spam and eggs
#abcd

print("======================================================")

# Ball grid solution
###################################################

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            canvas.draw_circle([2 * BALL_RADIUS * i + BALL_RADIUS, 2 * BALL_RADIUS * j + BALL_RADIUS], BALL_RADIUS, 1,
                               "white", "white")


# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

print("======================================================")

# Polyline drawing problem

###################################################

import math

polyline = []


# define mouseclick handler
def click(pos):
    polyline.append(pos)


# button to clear canvas
def clear():
    global polyline
    polyline = []


# define draw
def draw(canvas):
    if len(polyline) > 0:
        canvas.draw_circle(polyline[0], 1, 1, "White", "White")
        canvas.draw_polyline(polyline, 2, 'white')


# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()