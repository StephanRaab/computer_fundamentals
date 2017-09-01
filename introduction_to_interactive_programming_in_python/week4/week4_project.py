# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 400
HEIGHT = 600
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
score1 = 0
score2 = 0
color = "Limegreen"
horiz_vel = random.randrange(120, 240)
vert_vel = random.randrange(60, 180)
ball_vel = [horiz_vel / 20, vert_vel / 20]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
vel_incr = 7
ball_vel_incr = 1.1

paddle1_top_pos = [PAD_WIDTH / 2, 0]
paddle1_bottom_pos = [PAD_WIDTH / 2, PAD_HEIGHT]

paddle2_top_pos = [WIDTH - PAD_WIDTH / 2, 0]
paddle2_bottom_pos = [WIDTH - PAD_WIDTH / 2, PAD_HEIGHT]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [5, -2]
    else:
        ball_vel = [-5, -2]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.randrange(0, 2))
    score1 = 0
    score2 = 0


def draw(canvas):
    global score1, score2, ball_pos, ball_vel, BALL_RADIUS
    global paddle1_top_pos, paddle1_bottom_pos

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, color)
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, color)
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, color)

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] += ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] += ball_vel[1]
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and ball_pos[1] >= paddle1_top_pos[1] and ball_pos[1] <= \
            paddle1_bottom_pos[1]:
        ball_vel[0] = - ball_vel[0] * ball_vel_incr
        ball_pos[0] += ball_vel[0] * ball_vel_incr
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and ball_pos[1] >= paddle2_top_pos[1] and ball_pos[1] <= \
            paddle2_bottom_pos[1]:
        ball_vel[0] = - ball_vel[0] * ball_vel_incr
        ball_pos[0] += ball_vel[0] * ball_vel_incr
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        score1 += 1
        spawn_ball(LEFT)

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 4, color, color)

    # update paddle's vertical position, keep paddle on the screen
    paddle1_top_pos[1] += paddle1_vel[1]
    paddle1_bottom_pos[1] += paddle1_vel[1]
    if paddle1_top_pos[1] <= 0:
        paddle1_top_pos[1] = 0
        paddle1_bottom_pos[1] = PAD_HEIGHT
    if paddle2_top_pos[1] <= 0:
        paddle2_top_pos[1] = 0
        paddle2_bottom_pos[1] = PAD_HEIGHT

    paddle2_top_pos[1] += paddle2_vel[1]
    paddle2_bottom_pos[1] += paddle2_vel[1]
    if paddle1_bottom_pos[1] >= HEIGHT:
        paddle1_top_pos[1] = HEIGHT - PAD_HEIGHT
        paddle1_bottom_pos[1] = HEIGHT
    if paddle2_bottom_pos[1] >= HEIGHT:
        paddle2_top_pos[1] = HEIGHT - PAD_HEIGHT
        paddle2_bottom_pos[1] = HEIGHT

    # draw paddles
    canvas.draw_line(paddle1_top_pos, paddle1_bottom_pos, PAD_WIDTH, color)
    canvas.draw_line(paddle2_top_pos, paddle2_bottom_pos, PAD_WIDTH, color)

    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 2.5, 75], 60, color)
    canvas.draw_text(str(score2), [WIDTH / 1.75, 75], 60, color)

def keydown(key):
    global paddle1_vel, paddle2_vel, vel_incr
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = - vel_incr
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = vel_incr
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = - vel_incr
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = vel_incr


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)

# start frame
new_game()
frame.start()
