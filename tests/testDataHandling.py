# from src import dataLoader as DL
# from src import dataPreProcessor as DPP
# from src import partialSequenceAlignment as PSA
from tests import testHelper

# Test folder for data handling and processing. Run by executing the runTests.sh file in the root project directory.

####################################################
########## partialSequenceAlignment tests ##########
####################################################

def test_iterative_vs_recursive_rand_sample(TH, iterations=100, arr_size=50):
    from src import partialSequenceAlignment as PSA
    import numpy as np
    import random

    # create a test matching function
    def test_match_function(v1, v2):
        # If either of the passed values are None, this indicates that a value is being paired with a 'gap' character
        if v1 == None or v2 == None:
            return -1

        # If the absolute difference between the two values is less than 10, we award 1 point for matching, otherwise we award minus 1 points
        return 2 if abs(v1 - v2) <= 10 else -2

    # create numerous different data samples and compare the output of both partial sequence alignment approaches
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

def test_iterative_alignment(TH):
    from src import partialSequenceAlignment as PSA
    import numpy as np
    
    # create a test matching function, 1 for match, 0 otherwise (makes manually calculating optimal score easier)
    def test_match_function(v1, v2):
        # If either of the passed values are None, this indicates that a value is being paired with a 'gap' character
        if v1 == None or v2 == None:
            return 0

        # If the absolute difference between the two values is less than 10, we award 1 point for matching, otherwise we award minus 1 points
        return 1 if v1 == v2 else 0

    # perfect match
    test_seq_A = [1,2,3,4,5,6,7,8,9]
    test_seq_B = [1,2,3,4,5,6,7,8,9]
    iter_res = PSA.iterative_linear_space_partial_sequence_alignment(test_seq_A, test_seq_B, test_match_function)
    TH.test_equal("test_iterative_alignment_perfect", iter_res, len(test_seq_A))

    # no match
    test_seq_A = [1,1,1,1,1,1,1,1,1]
    test_seq_B = [0,0,0,0,0,0,0,0,0,0,0]
    iter_res = PSA.iterative_linear_space_partial_sequence_alignment(test_seq_A, test_seq_B, test_match_function)
    TH.test_equal("test_iterative_alignment_no_match", iter_res, 0)

    # offset match
    test_seq_A = [0,0,0,0,1,1,1,0,0,0,0]
    test_seq_B = [1,1,1,0,0,0,0,0,0]
    iter_res = PSA.iterative_linear_space_partial_sequence_alignment(test_seq_A, test_seq_B, test_match_function)
    TH.test_equal("test_iterative_alignment_minor_offset", iter_res, 7)

    # offset match, all of seq_B
    test_seq_A = [0,0,0,0,1,1,1,0,0,0,0]
    test_seq_B = [1,1,1]
    iter_res = PSA.iterative_linear_space_partial_sequence_alignment(test_seq_A, test_seq_B, test_match_function)
    TH.test_equal("test_iterative_alignment_offset_all_seq_B", iter_res, 3)

    # center mismatch
    test_seq_A = [0,0,0,0,1,1,1,1,4,5,6]
    test_seq_B = [9,9,1,1,1,0,4,5,6,9,9]
    iter_res = PSA.iterative_linear_space_partial_sequence_alignment(test_seq_A, test_seq_B, test_match_function)
    TH.test_equal("test_iterative_alignment_center_mismatch", iter_res, 6)

    # both have partial offset
    test_seq_A = [0,0,0,2,2,2,0]
    test_seq_B = [1,2,2,2,1,1,1,1,1,1,1]
    iter_res = PSA.iterative_linear_space_partial_sequence_alignment(test_seq_A, test_seq_B, test_match_function)
    TH.test_equal("test_iterative_alignment_partial_offset", iter_res, 3)

####################################################
####################################################
####################################################

# runs all tests
def run_tests():
    TH = testHelper.TestHelper()

    test_iterative_vs_recursive_rand_sample(TH)
    test_iterative_alignment(TH)

    TH.test_summary()

run_tests()
