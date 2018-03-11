
"""
Test suite for strategy_best in "Cookie Clicker"
"""
import poc_buildinfo_class as provided
import poc_simpletest

def run_suite(strategy_best):
    """
    Some informal testing code for strategy
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(simulate_clicker(provided.BuildInfo(), SIM_TIME, strategy_best), "produced 10000000000.0 total cookies", "Test #1:")

    suite.report_results()