"""
Test suite for strategy_cheap in "Cookie Clicker"
"""
import poc_buildinfo_class as provided
import poc_simpletest

def run_suite(strategy_cheap):
    """
    Some informal testing code for strategy
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(strategy_cheap(500000.0, 1.0, [(0.0, None, 0.0, 0.0)], 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15)),
    "expected A", "Test #1:")

    suite.report_results()
