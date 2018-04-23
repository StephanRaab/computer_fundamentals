"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def score_board(board, player):
    """
    Score a board
    """
    board_won_by = board.check_win()
    
    if board_won_by == None:
        return None
    else:
        if board_won_by == player:
            return SCORES[board_won_by]
        elif board_won_by == provided.DRAW:
            return SCORES[provided.DRAW]

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    sim_board = board.clone()
    current_score = score_board(sim_board, player)
         
    if current_score == 1:
        return 1, (-1,-1)
    if current_score == 0:
        return 0, (-1,-1)
    if current_score == -1:
        return -1, (-1,-1)
    else:
        empty_cells = sim_board.get_empty_squares()        
        child_board = {}
        
        for cell in empty_cells:
            board_child = sim_board.clone()
            board_child.move(cell[0], cell[1], player)
            
            new_current_score = score_board(board_child,player)
            if new_current_score == SCORES[player]:
                return new_current_score, cell
            child_board[cell] = board_child 
            
        max_score = current_score    
        cell_move = (-1,-1)
                
        for cell_key, board_value in child_board.items():
            child_board_cell_score = mm_move(board_value, provided.switch_player(player))
            if child_board_cell_score[0] * SCORES[player] >= max_score: 
                max_score = child_board_cell_score[0] * SCORES[player]
                cell_move = cell_key
                
        return  max_score * SCORES[player], cell_move 
             
def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

