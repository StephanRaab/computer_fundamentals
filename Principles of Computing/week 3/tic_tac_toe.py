"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

#import TEST_mc_update_scores

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 30        # Number of trials to run
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
    empty_squares = board.get_empty_squares()
    
    if board.check_win() == None:
        random_square = random.choice(empty_squares)
        board.move(random_square[0],random_square[1], player)
        player = provided.switch_player(player)
        mc_trial(board, player)
        
def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores (a list of lists) with
    the same dimensions as the Tic-Tac-Toe board, from a completed game,
    and which player the machine player is.
    Score the completed board and update the scores grid.
    Since function updates the scores grid directly, doesn't return anything
    """
    winner = board.check_win()
    mc_match = 0
    mc_other = 0
    
    if winner == player:
        mc_match = SCORE_CURRENT
        mc_other = -SCORE_OTHER
    elif winner == provided.switch_player(player):
        mc_match = -SCORE_CURRENT
        mc_other = SCORE_OTHER
        
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.square(row, col) == player:
                scores[row][col] += mc_match
            elif board.square(row, col) == provided.switch_player(player):
                scores[row][col] += mc_other

def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores.
    Find all of the empty squares with the maximum score
    and randomly return one of them as a (row, column) tuple.
    It is an error to call this function with a board that has
    no empty squares (there's no possible next move),
    so your function may do whatever it wants in that case.
    The case where the board is full will NOT be tested.
    """
    empty_squares = board.get_empty_squares()
    max_score = -float("inf")
    max_list = []
    
    if len(board.get_empty_squares()) == 0:
        print "No Empty Tiles Left!"
    else:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if scores[row][col] > max_score and (row, col) in empty_squares:
                    max_score = scores[row][col]
                    max_list = [row, col]
        max_tuple = (max_list[0], max_list[1])
    return max_tuple

def mc_move(board, player, trials):
    """
    Takes current board, which player the machine player is,
    and the number of trials to run.
    Use the Monte Carlo simulation to return a move for the machine player
    in the form of a (row, column) tuple.
    """
    scores = [[0 for dummy_i in range(board.get_dim())] 
            for dummy_i in range(board.get_dim())]
    
    for dummy_i in range(trials):
        clone_board = board.clone()
        mc_trial(clone_board, player)
        mc_update_scores(scores, clone_board, player)
    
    return get_best_move(board, scores)
    
#TEST_mc_update_scores.run_suite(mc_update_scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)      
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
