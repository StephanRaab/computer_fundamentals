# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 15
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True
COLOR = "Limegreen"

ball_pos = [WIDTH / 2, HEIGHT / 2]
score1 = 0
score2 = 0

horiz_vel = random.randrange(120, 240)
vert_vel = random.randrange(60, 180)
ball_vel = [horiz_vel / 20, vert_vel / 20]
vel_incr = 7
ball_vel_incr = 1.05

paddle1_pos = (HEIGHT/2) - (PAD_HEIGHT/2)
paddle2_pos = (HEIGHT/2) - (PAD_HEIGHT/2)
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction:
        ball_vel = [5, -2]
    else:
        ball_vel = [-5, -2]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    spawn_ball(random.randrange(0, 2))
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, ball_pos, ball_vel
    global paddle1_pos, paddle2_pos
    
    #draw paddles
    canvas.draw_line((0, paddle1_pos),(0, paddle1_pos + PAD_HEIGHT), PAD_WIDTH * 2, COLOR)
    canvas.draw_line((WIDTH, paddle2_pos),(WIDTH, paddle2_pos + PAD_HEIGHT), PAD_WIDTH * 2, COLOR)

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, COLOR)
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, COLOR)
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, COLOR)

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] += ball_vel[1]
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
        ball_vel[0] = - ball_vel[0] * ball_vel_incr
        ball_pos[0] += ball_vel[0] * ball_vel_incr
    if ball_pos[0] <= PAD_WIDTH  + BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
        ball_vel[0] = - ball_vel[0] * ball_vel_incr
        ball_pos[0] += ball_vel[0] * ball_vel_incr
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        score1 += 1
        spawn_ball(LEFT)

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 4, COLOR, COLOR)

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos <= 0:
        paddle1_pos = 0
    if paddle2_pos <= 0:
        paddle2_pos = 0

    paddle2_pos += paddle2_vel
    if paddle1_pos + PAD_HEIGHT >= HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    if paddle2_pos + PAD_HEIGHT >= HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
        
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 2.5, 75], 60, COLOR)
    canvas.draw_text(str(score2), [WIDTH / 1.75, 75], 60, COLOR)

def keydown(key):
    global paddle1_vel, paddle2_vel, vel_incr
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = - vel_incr
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel_incr
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = - vel_incr
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel_incr

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)

# start frame
new_game()
frame.start()
