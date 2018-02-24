import poc_simpletest

def run_suite(mc_move):
    """
    run code to test the mc_move function
    """
    suite = poc_simpletest.TestSuite()

    suite.run_test(mc_move("board", "player", 1), "expected result", "Test #1:")

    suite.report_results()