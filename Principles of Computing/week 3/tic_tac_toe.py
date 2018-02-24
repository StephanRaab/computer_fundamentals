"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    Takes current board and the next player to move.
    Play a game starting with the given player by making random moves,
    alternating between players.
    Return when the game is over.
    The modified board will contain the state of the game,
    Doesn't return anything, it modifies the board input.
    """
    pass

def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores (a list of lists) with
    the same dimensions as the Tic-Tac-Toe board, from a completed game,
    and which player the machine player is.
    Score the completed board and update the scores grid.
    Since function updates the scores grid directly, doesn't return anything
    """
    pass

def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores.
    Find all of the empty squares with the maximum score
    and randomly return one of them as a (𝚛𝚘𝚠, 𝚌𝚘𝚕𝚞𝚖𝚗) tuple.
    It is an error to call this function with a board that has
    no empty squares (there is no possible next move),
    so your function may do whatever it wants in that case.
    The case where the board is full will not be tested.
    """
    pass

def mc_move(board, player, trials):
    """
    Takes current board, which player the machine player is,
    and the number of trials to run.
    Use the Monte Carlo simulation to return a move for the machine player
    in the form of a (𝚛𝚘𝚠, 𝚌𝚘𝚕𝚞𝚖𝚗) tuple.
    Be sure to use the other functions you have written!
	"""
    pass

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
