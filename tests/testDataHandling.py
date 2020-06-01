# from src import dataLoader as DL
# from src import dataPreProcessor as DPP
# from src import partialSequenceAlignment as PSA
from tests import testHelper

# Test folder for data handling and processing. Run by executing the runTests.sh file in the root project directory.

def test_iterative_vs_recursive_rand_sample(TH, iterations=100, arr_size=50):
    from src import partialSequenceAlignment as PSA
    import numpy as np
    import random

    def test_match_function(v1, v2):
        # If either of the passed values are None, this indicates that a value is being paired with a 'gap' character
        if v1 == None or v2 == None:
            return -1

        # If the absolute difference between the two values is less than 10, we award 1 point for matching, otherwise we award minus 1 points
        return (2 if (abs(v1 - v2) < 10) else -2)

    for i in range(iterations):
        test_seq_A = [random.randint(0, 100) for n in range(random.randint(1,arr_size))]
        test_seq_B = [random.randint(0, 100) for n in range(random.randint(1,arr_size))]
        
        # Get array result from recursive partial sequence alignment
        res_arr = PSA.recursive_partial_sequence_alignment(test_seq_A, test_seq_B, test_match_function)
        recursive_res = res_arr.max()

        # Get max value result from iterative approach
        iter_res = PSA.iterative_linear_space_partial_sequence_alignment(test_seq_A, test_seq_B, test_match_function)


        # compare results
        TH.test_equal("test_iterative_vs_recursive", recursive_res, iter_res)

# runs all tests
def run_tests():
    TH = testHelper.TestHelper()

    test_iterative_vs_recursive_rand_sample(TH)

    TH.test_summary()

run_tests()
