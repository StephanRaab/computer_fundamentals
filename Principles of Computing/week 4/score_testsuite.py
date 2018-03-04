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
    
    # test gen_all_holds on various inputs
    hand = (1,)
    suite.run_test(score(hand), 1, "Test #1:")

    suite.report_results()