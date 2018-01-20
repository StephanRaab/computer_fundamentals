# Card game - Memory

import simplegui
import random
import math

TOTALCARDS = 16
CARD_COLOR = "green"
CARD_BORDER = "red"

turns = 0

WIDTH = TOTALCARDS * 50
HEIGHT = 100

# helper function to initialize globals
def new_game():
    global state, cardnum, exposed_list, comparison, turns
    state = 0
    turns = 0
    cardnum = range(0,TOTALCARDS//2)
    cardnum2 = range(0,TOTALCARDS//2)
    cardnum.extend(cardnum2)
    random.shuffle(cardnum)
    exposed_list = []
    comparison = []
    label.set_text("Turns = " + str(turns))

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed_list, comparison, state, turns
    position = (pos[0] // 50)

    if position in exposed_list or position in comparison:
        turns = turns
    else:
        label.set_text("Turns = " + str(turns))
        if state == 0:
            state = 1
            turns += 1
            comparison.append(position)
        elif state == 1:
            state = 2
            comparison.append(position)
            if cardnum[comparison[0]] == cardnum[comparison[1]]:
                exposed_list.append(comparison[0])
                exposed_list.append(comparison[1])
        else:
            state = 1
            comparison = []
            comparison.append(position)
            turns += 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    init_card = 13
    card_pos = 0
    for num in range(len(cardnum)):
        canvas.draw_text(str(cardnum[num]), (init_card, HEIGHT//1.6), 40, "White")
        
        def draw_cards():
            canvas.draw_polygon([(card_pos, 0), (card_pos + 50, 0),
                         (card_pos + 50,HEIGHT), (card_pos, HEIGHT)], 2, CARD_BORDER, CARD_COLOR)
  
        if state == 0:
            draw_cards()    
        if state == 1:        
            if not int(card_pos//50) in exposed_list and not int(card_pos//50) in comparison:
                draw_cards()
        if state == 2:
            if not int(card_pos//50) in exposed_list and not int(card_pos//50) in comparison:
                draw_cards()
        init_card += 50
        card_pos += 50


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
