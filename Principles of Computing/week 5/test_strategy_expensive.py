"""
Test suite for strategy_expensive in "Cookie Clicker"
"""
import poc_buildinfo_class as provided
import poc_simpletest

def run_suite(strategy_expensive):
    """
    Some informal testing code for strategy
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(strategy_expensive(500000.0, 1.0, [(0.0, None, 0.0, 0.0)], 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15)),
    "expected C", "Test #1:")

    suite.report_results()