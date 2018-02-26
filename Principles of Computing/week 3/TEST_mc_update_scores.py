import poc_simpletest
import poc_ttt_provided as provided

def run_suite(mc_update_scores):
    """
    run code to test the mc_update_scores function
    """
    suite = poc_simpletest.TestSuite()

    suite.run_test(mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 2),[[1.0, 1.0, -1.0], [-1.0, 1.0, 0], [0, 1.0, -1.0]], "Test #1: ")
    suite.run_test(mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 3),[[-1.0, -1.0, 1.0], [1.0, -1.0, 0], [0, -1.0, 1.0]], "Test #2: ")

    suite.report_results()
