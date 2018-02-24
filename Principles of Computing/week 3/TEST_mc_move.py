import poc_simpletest
import poc_ttt_provided as provided

board = provided.TTTBoard(3, False, None)
PLAYERX = provided.PLAYERX


def run_suite(mc_move):
    """
    run code to test the mc_move function
    """
    suite = poc_simpletest.TestSuite()

    suite.run_test(mc_move(board, PLAYERX, 1), (0,0), "Test #1:")
    # suite.run_test(mc_move(board, PLAYERX, 1), (0,1), "Test #2:")
    # suite.run_test(mc_move(board, PLAYERX, 1), (0,2), "Test #3:")
    # suite.run_test(mc_move(board, PLAYERX, 1), (1,0), "Test #4:")
    # suite.run_test(mc_move(board, PLAYERX, 1), (1,1), "Test #5:")
    # suite.run_test(mc_move(board, PLAYERX, 1), (1,2), "Test #6:")
    # suite.run_test(mc_move(board, PLAYERX, 1), (2,0), "Test #7:")
    # suite.run_test(mc_move(board, PLAYERX, 1), (2,1), "Test #8:")
    # suite.run_test(mc_move(board, PLAYERX, 1), (2,2), "Test #9:")

    suite.report_results()