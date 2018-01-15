# Card game - Memory

import simplegui
import random
import math

TOTALCARDS = 16
CARD_COLOR = "green"
CARD_BORDER = "red"

WIDTH = TOTALCARDS * 50
HEIGHT = 100
turns = 0

# helper function to initialize globals
def new_game():
    global state, cardnum, exposed_list, comparison
    state = 0
    cardnum = range(0,TOTALCARDS//2)
    cardnum2 = range(0,TOTALCARDS//2)
    cardnum.extend(cardnum2)
    random.shuffle(cardnum)
    exposed_list = []
    comparison = []
    print "Cards:", cardnum

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed_list, comparison, state, turns
    position = int(math.floor(pos[0] / 50.0))
    if position in exposed_list:
        turns = turns
        label.set_text("Turns = " + str(turns))
    else:
        label.set_text("Turns = " + str(turns))
        if state == 0:
            state = 1
            comparison.append(position)
            print "state:",state
            print "comparison", comparison
        elif state == 1:
            state = 2
            comparison.append(position)
            print "state:",state
            print "comparison", comparison
            if cardnum[comparison[0]] == cardnum[comparison[1]]:
                exposed_list.append(comparison[0])
                exposed_list.append(comparison[1])
                print "exposed", exposed_list
                comparison = []
            else:
                comparison = []
        else:
            state = 1
            comparison.append(position)
            turns += 1
        
    print comparison
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    init_card = 13
    card_start = 0
    for num in cardnum:
        canvas.draw_text(str(num), (init_card, HEIGHT//1.6), 40, "White")
        
        if state == 0:
            #hide everything
                canvas.draw_polygon([(card_start, 0), (card_start + 50, 0),
                         (card_start + 50,HEIGHT), (card_start, HEIGHT)], 2, CARD_BORDER, CARD_COLOR)
        if state == 1:        
            #1 hide everything that isn't exposed
            if not int(math.floor(card_start/50)) in exposed_list:
                canvas.draw_polygon([(card_start, 0), (card_start + 50, 0),
                                    (card_start + 50,HEIGHT), (card_start, HEIGHT)], 2, CARD_BORDER, CARD_COLOR)
            #2 show current clicked card
#            if not int(math.floor(card_start/50)) in comparison or exposed_list:
#                canvas.draw_polygon([(card_start, 0), (card_start + 50, 0),
#                                     (card_start + 50,HEIGHT), (card_start, HEIGHT)], 2, CARD_BORDER, CARD_COLOR)
        if state == 2:
            #1 hide everything that isn't exposed
            if not int(math.floor(card_start/50)) in exposed_list:
                canvas.draw_polygon([(card_start, 0), (card_start + 50, 0),
                                    (card_start + 50,HEIGHT), (card_start, HEIGHT)], 2, CARD_BORDER, CARD_COLOR)
            #2 show current clicked card
#            if int(math.floor(card_start/50)) not in comparison:
#                canvas.draw_polygon([(card_start, 0), (card_start + 50, 0),
#                                     (card_start + 50,HEIGHT), (card_start, HEIGHT)], 2, CARD_BORDER, CARD_COLOR)
        init_card += 50
        card_start += 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric