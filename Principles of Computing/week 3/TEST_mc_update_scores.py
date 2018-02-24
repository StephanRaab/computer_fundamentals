import poc_simpletest

def run_suite(mc_update_scores):
    """
    run code to test the mc_update_scores function
    """
    suite = poc_simpletest.TestSuite()

    suite.run_test(mc_update_scores("scores", "board", "player"), "expected", "Test #1:")

    suite.report_results()