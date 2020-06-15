# This file provides functionality to create a suffix tree from a sequence of data.


def build_suffix_tree(data, compress_size=1, compress_func=None):
    """
	Description: Takes sequence data and creates a suffix tree
	Context: Helps in the process of aligning with multiple sequence simultaneously
	Parameters:
		{data} Array[Array] : A 2D array containing sequence data. All sequences will be added to the suffix tree
        {compress_size} int : The ratio between the input data and the data stored in the suffix tree. i.e. if compress_size = 2, every 2 data points in the input will
                                be converted into a single value to put into the suffix tree.
        {compress_func} function : takes and array argument and returns a single value ouput. If no function is provided, will compress with a default mean calculator.
	Return:
		{ST_object} : Suffix Tree object
	"""
    return None