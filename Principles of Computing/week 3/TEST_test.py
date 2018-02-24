import poc_simpletest

def run_suite(addition):
    """
    run code to test the addition function
    """
    suite = poc_simpletest.TestSuite()

    suite.run_test(addition(2, 2), 4, "Test #1:")
    suite.run_test(addition(2, 1), 3, "Test #2:")
    suite.run_test(addition(500,502), 1002, "Test #3:")
    suite.run_test(addition(28, 29), 57, "Test #4:")

    suite.report_results()