# Print to canvas
###################################################
import simplegui

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!", [120, 112], 48, "Red")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)
frame.set_draw_handler(draw)

frame.start()

# Display "This is easy?"
###################################################
import simplegui

# Draw handler
def draw(canvas):
    canvas.draw_text("This is easy", [100,115], 48, "Green")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

# Display an X
###################################################
import simplegui

# Draw handler
def draw(canvas):
    canvas.draw_text("X", [0,35], 48, "White")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("X Drawing", 96, 96)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


# Define a function that returns formatted minutes and seconds
###################################################
# Time formatting function
def format_time(random_num):
    minutes = str(random_num // 60)
    seconds = str(random_num % 60)
    return (minutes + " minutes and " + seconds + " seconds")

###################################################
# Tests
print(format_time(23))
print(format_time(1237))
print(format_time(0))
print(format_time(1860))

# Move a ball
###################################################
import simplegui

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH // 2, HEIGHT // 2], ball_radius, 1, "White", "White")

# Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius += RADIUS_INCREMENT

def decrease_radius():
    global ball_radius
    if ball_radius > RADIUS_INCREMENT:
        ball_radius -= RADIUS_INCREMENT

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)

# Start the frame animation
frame.start()