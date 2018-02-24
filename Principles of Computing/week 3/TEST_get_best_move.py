import poc_simpletest

def run_suite(get_best_move):
    """
    run code to test the mc_move function
    """
    suite = poc_simpletest.TestSuite()

    suite.run_suite(get_best_move("board", "scores"), "expected outcome", "Test #1: ")

    suite.report_results