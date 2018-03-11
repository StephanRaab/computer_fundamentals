"""
Test suite for time_until in "Cookie Clicker"
"""
import poc_buildinfo_class as provided
import poc_simpletest

def run_suite(time_until):
    """
    Some informal testing code for strategy
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(time_until(47.0), 2.0, "Test #1:")

    suite.report_results()