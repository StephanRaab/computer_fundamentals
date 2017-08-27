#version 1

# # Implementation of classic arcade game Pong
#
# import simplegui
# import random
#
# # initialize globals - pos and vel encode vertical info for paddles
# WIDTH = 600
# HEIGHT = 400
# BALL_RADIUS = 20
# PAD_WIDTH = 8
# PAD_HEIGHT = 80
# HALF_PAD_WIDTH = PAD_WIDTH / 2
# HALF_PAD_HEIGHT = PAD_HEIGHT / 2
# LEFT = False
# RIGHT = True
# ball_pos = [0, 0]
# ball_vel = [0, 0]
# paddle1_pos = [HALF_PAD_WIDTH, HALF_PAD_HEIGHT]
# paddle2_pos = [WIDTH, ]
# paddle_speed = 0.5
# paddle1_vel = 0
# paddle2_vel = 0
# score_1 = 0
# score_2 = 0
#
#
# # initialize ball_pos and ball_vel for new bal in middle of table
# # if direction is RIGHT, the ball's velocity is upper right, else upper left
# def spawn_ball(direction):
#     global ball_pos, ball_vel  # these are vectors stored as lists
#     ball_pos = [WIDTH / 2, HEIGHT / 2]
#     ball_vel = [0, 0]
#     if direction == RIGHT:
#         ball_vel[0] = 1
#     else:
#         ball_vel[0] = -1
#
#
# # define event handlers
# def new_game():
#     global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
#     global score1, score2  # these are ints
#     spawn_ball(RIGHT)
#
#
# def draw(canvas):
#     global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
#
#     # draw mid line and gutters
#     canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
#     canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
#     canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
#
#     # update ball
#
#     # draw ball
#     canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "white", "white")
#
#     # update paddle's vertical position, keep paddle on the screen
#
#     # draw paddle
#     paddle1 = canvas.draw_polygon([[0, 0], [0, PAD_HEIGHT]], PAD_WIDTH, "white", "white")
#     paddle2 = canvas.draw_polygon([[WIDTH, 0], [WIDTH, PAD_HEIGHT]], PAD_WIDTH, "white", "white")
#
#
#     # determine whether paddle and ball collide
#
#     # draw scores
#
#
# def keydown(key):
#     global paddle1_vel, paddle2_vel, paddle_speed
#     paddle1_vel += paddle_speed
#     paddle2_vel += paddle_speed
#
#
# def keyup(key):
#     global paddle1_vel, paddle2_vel
#     paddle1_vel = 0
#     paddle2_vel = 0
#
#
# # create frame
# frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
# frame.set_draw_handler(draw)
# frame.set_keydown_handler(keydown)
# frame.set_keyup_handler(keyup)
#
# # start frame
# new_game()
# frame.start()


#version 2
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]

horiz_vel = random.randrange(120, 240)
vert_vel = random.randrange(60, 180)
ball_vel = [horiz_vel, vert_vel]

test_vel = [2, 3]


def tick():
    global time
    time += 1


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, test_vel, BALL_RADIUS

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += test_vel[0]
    ball_pos[1] += test_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        test_vel[1] = - test_vel[1]
        ball_pos[1] += test_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        test_vel[1] = - test_vel[1]
        ball_pos[1] += test_vel[1]
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        test_vel[0] = - test_vel[0]
        ball_pos[0] += test_vel[0]
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        test_vel[0] = - test_vel[0]
        ball_pos[0] += test_vel[0]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "white", "white")

    # update paddle's vertical position, keep paddle on the screen

    # draw paddles

    # determine whether paddle and ball collide

    # draw scores


def keydown(key):
    global paddle1_vel, paddle2_vel


def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
