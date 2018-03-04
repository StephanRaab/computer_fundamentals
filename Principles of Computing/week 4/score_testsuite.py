"""
Test suite for score in "Yahtzee"
"""
import poc_simpletest

def run_suite(score):
    """
    Some informal testing code for score
    """
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test score  on various inputs
    hand = (1,)
    suite.run_test(score(hand), 1, "Test #1:")

    hand = (1,1,1,5,6)
    suite.run_test(score(hand), 6, "Test #2:")

    hand = (2,2,4,2,5)
    suite.run_test(score(hand), 6, "Test #3:")

    hand = (4,3,5,5,2)
    suite.run_test(score(hand), 10, "Test #4:")

    suite.report_results()