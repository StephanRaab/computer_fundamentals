"""
Test suite for expected_value in "Yahtzee"
"""

import poc_simpletest

def run_suite(expected_value):
    """
    Some informal testing code for expected_value
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test gen_all_holds on various inputs
    held_dice = (2,2)
    num_die_sides = 6
    num_free_dice = 2
    suite.run_test(expected_value(held_dice, num_die_sides, num_free_dice), 5.833333333333, "Test #1:")

    suite.report_results()