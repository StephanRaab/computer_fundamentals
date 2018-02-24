import poc_simpletest

def run_suite(mc_trial):
    """
    run code to test the mc_trial function
    """
    suite = poc_simpletest.TestSuite()

    suite.run_test(mc_trial("board", "player"), "expected", "Test #1:")

    suite.report_results()