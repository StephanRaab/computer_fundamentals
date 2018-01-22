# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
win_or_lose = ""
score = 0
deck = []
player_hand = []
dealer_hand = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
       
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand_list = []

    def __str__(self):
        # return a string representation of a hand
        string = "Hand contains "
        for card in self.hand_list:
            string += str(card) + " "
        return string

    def add_card(self, card):
        # add a card object to a hand
#        self.hand_list.append(card.suit + card.rank)
        self.hand_list.append(card)    
    
    def get_value(self):
        value = 0
        ace_count = 0
        for card in self.hand_list:
            if card.get_rank() == 'A':
                ace_count += 1
            value += VALUES[card.get_rank()]
            
        if ace_count < 1:
            return value
        else:
            if value + 10 <= 21:
                return value + 10
            else:
                return value     
   
    def draw(self, canvas, ypos):
        # draw a hand on the canvas, use the draw method for cards  
        x_incr = 75
        x_start = 50
        for card in self.hand_list:
            card.draw(canvas, [x_start, ypos])
            x_start += 75
        canvas.draw_image(card_back, [0,0], CARD_BACK_SIZE, [CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
     
#   card = Card("H", "A")

           
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_list = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_list.append(Card(suit,rank))
        return self.deck_list
    
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        return random.shuffle(self.deck_list)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck_list.pop()

    def __str__(self):
        # return a string representing the deck
        return "Deck contains " + str(self.deck_list)

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, outcome
    deck = Deck()
    outcome = "Hit or Stand?"
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    in_play = True

def hit():
    global in_play, deck, player_hand, dealer_hand, score, outcome, win_or_lose
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        player_value = player_hand.get_value()
        if player_value > 21:
            # if busted, assign a message to outcome, update in_play and score
            in_play = False
            outcome = "New deal?"
            win_or_lose = "You lost."
            score -= 1
           
def stand():
    global in_play, score, outcome, win_or_lose
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        dealer_value = dealer_hand.get_value()
        player_value = player_hand.get_value()
        while dealer_value < 17:
            dealer_hand.add_card(deck.deal_card())
            dealer_value = dealer_hand.get_value()
        if dealer_value > 21:
            in_play = False
            score += 1
            outcome = "New deal?"
            win_or_lose = "You won!"
        else:
            if dealer_value > player_value or dealer_value == player_value:
                in_play = False
                score -= 1
                outcome = "New deal?"
                win_or_lose = "You lost."
            else:
                in_play = False
                score += 1
                outcome = "New deal?"
                win_or_lose = "You won!"
    else:
        outcome = "You have busted"     

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (200, 50), 40, "black", 'sans-serif')
    canvas.draw_text(str(score), (500, 50), 40, "black", 'sans-serif')
    canvas.draw_text("Dealer", (50, 100), 24, "black", 'sans-serif')
    canvas.draw_text(win_or_lose, (200, 100), 24, "black", "sans-serif")
    canvas.draw_text("Player", (50, 300), 24, "black", 'sans-serif')
    canvas.draw_text(outcome, (200, 300), 24, "black", 'sans-serif')        
    player_hand.draw(canvas, 320)
    if in_play:
        dealer_hand.draw(canvas, 120)
    else:
        dealer_hand.draw(canvas, 120)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
