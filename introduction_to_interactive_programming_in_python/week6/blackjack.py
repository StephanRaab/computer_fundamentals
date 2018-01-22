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
    def __init__(self):
        # create Hand object
        self.hand_list = []

    def __str__(self):
        # return a string representation of a hand            
        return "Hand contains " + str(self.hand_list)

    def add_card(self, card):
        # add a card object to a hand
        self.hand_list.append(card.suit + card.rank)
#        self.hand_list.append(card)    
    
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value
        # if it doesn't bust compute the value of the hand, see Blackjack video
        value = 0
        ace_count = 0
        for card in self.hand_list:
            if card[1] == 'A':
                ace_count += 1
            value += VALUES[card[1]]
            
        if ace_count < 1:
            return value
        else:
            if value + 10 <= 21:
                return value + 10
            else:
                return value
                   
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_list = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_list.append(suit + rank)
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
    global outcome, in_play, deck, player_hand, dealer_hand
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    print "Player", player_hand    
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print "Dealer", dealer_hand

    in_play = True

def hit():
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


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


# remember to review the gradic rubric