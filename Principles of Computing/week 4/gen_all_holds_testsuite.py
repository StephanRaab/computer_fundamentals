"""
Test suite for gen_all_holds in "Yahtzee"
"""

import poc_simpletest

def run_suite(gen_all_holds):
    """
    Some informal testing code for gen_all_holds
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test gen_all_holds on various inputs
    hand = (1,)
    suite.run_test(gen_all_holds(hand), set([(), (1,)]), "Test #1:")

    suite.report_results()