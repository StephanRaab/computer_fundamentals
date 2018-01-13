# "Stopwatch: The Game"

import simplegui

# define global variables
WIDTH = 300
HEIGHT = 300
userGuess = 0
totalGuess = 0
ticker = 0
tenths = 0
secA = 0
secB = 0
secC = 0
mins = 0
stopwatch = "0:00.0"
game = "0/0"
gameColor = "White"
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(ticker):
    global tenths, secA, secB, mins, stopwatch
    tenths = ticker % 10
    secA = (ticker // 10) % 10
    secB = ticker // 10
    secC = (secB // 10) % 6
    mins = secB // 60
    stopwatch = str(mins) + ":" + str(secC) + str(secA) + "." + str(tenths)
    return stopwatch

def tick():
    global ticker
    ticker += 1
    format(ticker)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    stopped = False
    timer.start()

def stop():
    global userGuess, totalGuess, game, gameColor, stopped
    timer.stop()
    
    if not stopped:
        totalGuess += 1
        if tenths == 0:
            userGuess += 1
            gameColor = "Green"
            stopped = True
        else:
            gameColor = "Red"
            stopped = True
        
    game = str(userGuess) + "/" + str(totalGuess)
    
def reset():
    global ticker, userGuess, totalGuess, game, gameColor, stopped
    stopped = True
    timer.stop()
    ticker = 0
    userGuess = 0
    totalGuess = 0
    game = "0/0"
    gameColor = "White"
    format(ticker)
    
# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, tick)

# define draw handler
def draw(canvas):
    canvas.draw_text(stopwatch, [(WIDTH/2) - 50, HEIGHT/2], 40, "White")
    canvas.draw_text(game, [WIDTH - 40, 25], 20, gameColor)
    
# create frame
frame = simplegui.create_frame("StopWatch: The Game", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# start frame
frame.start()
