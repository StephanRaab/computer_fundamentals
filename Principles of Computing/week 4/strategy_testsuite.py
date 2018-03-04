"""
Test suite for strategy in "Yahtzee"
"""

import poc_simpletest

def run_suite(strategy):
    """
    Some informal testing code for strategy
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test gen_all_holds on various inputs
    hand = (1,)
    num_sides = 6
    suite.run_test(strategy(hand, num_sides), (3.5, ()), "Test #1:")

    suite.report_results()