
# Basic partial sequence alignment functionality
import numpy as np
import dataLoader
import dataPreProcessor

def partial_sequence_alignment(sequence_A, sequence_B):
    """
	Description: Recursive n^2 implementation of partial sequence alignment matching between two provided sequences
	Context: Useful as 'proof of cocnept' testing for sequence alignment between byte strings
    Warning: Do not use for sizeable inputs or practice. Inefficient memory and time requirements
	Parameters:
		{sequence_A} ByteString : ByteString of music data
        {sequence_B} ByteString : ByteString of music data
	Return:
		{ndarray} : Numpy array of the resulting score matrix
	"""

    # Initialize OPT array, this is where we will store our sequence alignment scoring
    opt_arr = np.zeros((len(sequence_A), len(sequence_B)))

    # Initialize mask, this tells us if we have already calculated a value
    mask = np.zeros(opt_arr.shape)
    calc_opt(sequence_A, sequence_B, opt_arr, len(sequence_A)-1,len(sequence_B)-1, mask)
    return opt_arr

def match_value(v1, v2):
    """
	Description: Basic scoring between two provided values
	Context: When performing partial sequence alignment, we need to be able to score the matching of two elements of the provided sequence, or the matching of a single element with a gap
	Parameters:
		{v1} byte/None : ByteString of music data
        {v1} byte/None : ByteString of music data
	Return:
		{Integer} : Integer scoring value (positive is better, negative is worse)
	"""

    # If either of the passed values are None, this indicates that a value is being paired with a 'gap' character
    if v1 == None or v2 == None:
        return -1

    # If the absolute difference between the two values is less than 10, we award 1 point for matching, otherwise we award minus 1 points
    return (2 if (abs(v1 - v2) < 10) else -2)

def calc_opt(seq_A, seq_B, arr, i, j, mask):
    """
	Description: Calculates the optimal partial alignment between seq_A and seq_B. The below DP solution below works by allowing the matching of the suffix of the prefix of both sequences.
        In other terms, we are matching seq_A[0:i] with seq_B[0:j], but allow the cost of any prefix of seq_A[0:i] or seq_B[0:j] to be zero. Thus, only the scores from the suffixes of 
        seq_A[0:i] and seq_B[0:j] will be counted. The recurrence relation is as follows: 
        Opt[i,j] = max(
                    OPT(i-1,j-1) + S(i,j), 
                    OPT(i,j-1) + S(-, j), 
                    OPT(i-1, j) + S(i,-), 
                    0
                    )
        Where S is a scoring function, and '-' represents matching to a gap
	Context: Using dynamic programming, we can perform a partial sequence alignment between two sequences. This is slow and will not scale well with input size, but can be useful for basic testing
        and small-case verification
	Parameters:
		{seq_A} ByteString : ByteString of music data
        {seq_B} ByteString : ByteString of music data
        {arr} ndarray : OPT array we are filling with calculated scores
        {i} Integer : Our current prefix of seq_A, i.e. seq_A[0:i]
        {j} Integer : Our current prefix of seq_B, i.e. seq_B[0:j]
	Return:
		{Integer} : The resulting opt value for the partial sequence alignment of seq_A[0:i] and seq_B[0:j]
	"""
    
    # If out of bounds, return 0
    if i < 0 or j < 0:
        return 0

    # If this value has already been calculated, return it
    if mask[i][j] == 1:
        return arr[i][j]

    # Set this value as calculated
    mask[i][j] = 1

    # Calculate the optimal value for this index in the opt arry
    potential_val_1 = calc_opt(seq_A, seq_B, arr, i-1, j-1, mask) + match_value(seq_A[i], seq_B[j]) # Assumes we match the two characters at index i and j
    potential_val_2 = calc_opt(seq_A, seq_B, arr, i, j-1, mask)   + match_value(None,   seq_B[j]) # Assumes we pair the character at j with a gap
    potential_val_3 = calc_opt(seq_A, seq_B, arr, i-1, j, mask)   + match_value(seq_A[i],   None) # Assumes we pair the character at i with a gap

    # Choose the highest value out
    opt_choice = max(potential_val_1, potential_val_2, potential_val_3, 0)

    # Set this value in our opt array
    arr[i][j] = opt_choice
    return arr[i][j]

# Iterative linear memory calculation will only allow us to display a maximum score for the partial matching, not the matched location itself (other than the i,j lcoation of the end of the prefix)
def iterative_linear_space_partial_sequence_alignment(seq_A, seq_B, match_function):
    len_seq_A = len(seq_A)
    len_seq_B = len(seq_B)

    # Based off of our DP recursive relationship, we do not require to store the entire n by m matrix.
    opt_arr = np.zeros((2, len_seq_B))
    
    # the current maximum partial alignment score in our matrix
    curr_max = 0

    # the current row in our opt_arr that we are calculating values for, we will be over writting the previous values stored here
    curr_row = 1
    prev_row = 0

    # at each iteration of the loop, we will be matching the partial alignment of seq_A[0:seq_A_suffix] to seq_B[0:seq_B_suffix]
    for seq_A_suffix in range(len_seq_A):
        
        # update our current and previous row
        curr_row = 0 if curr_row == 1 else 1
        prev_row = 0 if prev_row == 1 else 1

        for seq_B_suffix in range(len_seq_B):

            # calculate the score of matching the last elements of the suffix together
            previous_opt_val_match = 0 if seq_B_suffix - 1 < 0 else opt_arr[prev_row][seq_B_suffix-1] # previous opt value if we were to match the two current elements
            match_pair_score = match_function(seq_A[seq_A_suffix], seq_B[seq_B_suffix]) # the matching score related to matching these two elements
            match_pair_value = previous_opt_val_match + match_pair_score # the final value of this pairing

            # calculate the score of matching the last element of seq_A with a gap
            previous_opt_val_gapA = opt_arr[prev_row][seq_B_suffix] # previous opt value if we were to match the current element of seq_A with a gap
            match_gapA_score = match_function(seq_A[seq_A_suffix], None) # the matching score related to matching the current element of seq_A with a gap
            match_gapA_value = previous_opt_val_gapA + match_gapA_score # the final value of this pairing

            # calculate the score of matching the last element of seq_B with a gap
            previous_opt_val_gapB = 0 if seq_B_suffix - 1 < 0 else opt_arr[curr_row][seq_B_suffix-1] # previous opt value if we were to match a gap with the current element of seq_B
            match_gapB_score = match_function(None, seq_B[seq_B_suffix]) # the matching score related to matching a gap with the current element of seq_B
            match_gapB_value = previous_opt_val_gapB + match_gapB_score # the final value of this pairing

            # choose the max value to set into our opt_arr
            opt_arr[curr_row][seq_B_suffix] = max(match_pair_value, match_gapA_value, match_gapB_value)
            
            # update our current maximum pairwise alignment score
            curr_max = max(curr_max, opt_arr[curr_row][seq_B_suffix])

    return curr_max


