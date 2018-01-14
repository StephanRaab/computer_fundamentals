# implementation of card game - Memory

import simplegui
import random

TOTALCARDS = 16
CARD_COLOR = "green"
CARD_BORDER = "red"

WIDTH = TOTALCARDS * 50
HEIGHT = 100

cardnum = range(0,TOTALCARDS//2)
cardnum2 = range(0,TOTALCARDS//2)
cardnum.extend(cardnum2)
random.shuffle(cardnum)
exposed_list = []

print "Cards: ", cardnum

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    
    pass
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    init_card = 13
    card_start = 0
    for i in cardnum:
        canvas.draw_text(str(cardnum[i]), (init_card, HEIGHT//1.6), 40, "White") 
        canvas.draw_polygon([(card_start, 0), (card_start + 50, 0),
                             (card_start + 50,HEIGHT), (card_start, HEIGHT)], 2, CARD_BORDER, CARD_COLOR)
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