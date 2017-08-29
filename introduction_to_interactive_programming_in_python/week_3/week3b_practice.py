# Counter ticks
###################################################

import simplegui

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)

timer.start()

# Counter with buttons
###################################################
import simplegui

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1


# Event handlers for buttons
def start():
    timer.start()


def stop():
    timer.stop()


def reset():
    global counter
    counter = 0

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()

# Counter with buttons
###################################################
import simplegui

color = "Red"

# Timer handler
def tick():
    global color
    if color == "Red":
        color = "Blue"
    else:
        color = "Red"
    frame.set_canvas_background(color)

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.set_canvas_background(color)
timer = simplegui.create_timer(1000, tick)

# Start timer
frame.start()
timer.start()

# Expanding circle by timer
###################################################
import simplegui

WIDTH = 400
HEIGHT = 400
radius = 1

# Timer handler
def tick():
    global radius
    radius += 1

# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH // 2, HEIGHT // 2], radius, 5, "Blue", "White")

# Create frame and timer
frame = simplegui.create_frame("Circle Timer", WIDTH, HEIGHT)
timer = simplegui.create_timer(100, tick)

# Start timer
frame.start()
frame.set_draw_handler(draw)
timer.start()

# Reflex tester
###################################################
import simplegui

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1

# Button handler
def click():
    global total_ticks, first_click
    if first_click:
        first_click = False
        total_ticks = 0
        timer.start()
    else:
        first_click = True
        timer.stop()
        print("Time between ticks was " + str(total_ticks / 100.0) + " seconds")
        total_ticks = 0

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()