# "Stopwatch: The Game"
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
time = 0
HEIGHT = 300
WIDTH = 300
SUCCESSCOUNTER = 0
TOTALSTOPS = 0
is_stopwatch_running = False
is_stop_clicked = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# A should be zero if < minute, B should be zero < 10 seconds
def format(time):
    if time == 0:
        return str("0:00.0")
    elif time < 10:
        return str("0:00." + str(time))
    elif time >= 10:
        tenths = time % 10
        str_seconds = str(time)[0:-1]
        seconds = int(str_seconds) % 60
        minutes = time // 600
        if seconds < 10:
            return str(str(minutes) + ":0" + str(seconds) + "." + str(tenths))
        return str(str(minutes) + ":" + str(seconds) + "." + str(tenths))

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_stopwatch_running
    global is_stop_clicked
    is_stopwatch_running = True
    is_stop_clicked = False
    timer.start()

def stop():
    global TOTALSTOPS
    global SUCCESSCOUNTER
    global is_stopwatch_running
    global is_stop_clicked
    timer.stop()
    is_stopwatch_running = False
    if time == 0:
        TOTALSTOPS == 0
    elif time % 10 == 0 and is_stop_clicked == False:
        SUCCESSCOUNTER += 1
        TOTALSTOPS += 1
        is_stop_clicked = True
    elif time % 10 != 0 and is_stop_clicked == False:
        TOTALSTOPS += 1
        is_stop_clicked = True

def reset():
    global time
    global TOTALSTOPS
    global SUCCESSCOUNTER
    global is_stopwatch_running
    time = 0
    timer.stop()
    is_stopwatch_running = False
    SUCCESSCOUNTER = 0
    TOTALSTOPS = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(time)), [WIDTH / 5, HEIGHT / 1.8], 72, "Lime")
    canvas.draw_text(str(SUCCESSCOUNTER),[WIDTH / 2 - 15, 35], 36, "White")
    canvas.draw_text(str(TOTALSTOPS),[WIDTH / 2 + 15, 35], 36, "Red")

# create frame
frame = simplegui.create_frame("Counter with buttons", WIDTH, HEIGHT)

# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
frame.set_draw_handler(draw)