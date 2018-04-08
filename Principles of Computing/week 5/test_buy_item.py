"""
Test suite for buy_item in "Cookie Clicker"
"""
import poc_buildinfo_class as provided
import poc_simpletest

def run_suite(buy_item):
    """
    Some informal testing code for strategy
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(buy_item('item', 1.0, 3.5), , "Test #1:")

    suite.report_results()