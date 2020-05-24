# This file provides functionality for processing a provided AudioSegment object into a more useable format, also provides auxillary debugging and information tools

from pydub import AudioSegment
import dataLoader

def AudioSegment_details(AS_object):
	"""
	Description: This functtion will print general data about the provided AudioSegment file
	Context: When debugging or attempting to modify files, easy access to an info sheet is useful
	Parameters:
		{AS_object} AudioSegment : AudioSegment object
	Return:
		NA
	"""

	# Verify the correct object type is passed
	if not AudioSegment_verify(AS_object):
		raise Exception("Provided invalid object type")

	# Data we will be displaying
	audio_duration = AS_object.duration_seconds # duration of the audio sample ins econds
	sample_length = len(AS_object) # length of the sample in bytes
	channel_count = AS_object.channels # how many channels are in the audio sample
	max_amplitude = AS_object.max # maximum amplitude across the entire sample
	raw_data_sample = AudioSegment_raw(AS_object)[0:min(8,len(AS_object))] # a sample of the raw data, in the form of a byte string
	raw_data_type = type(raw_data_sample) # type of raw data, should always be 'bytes'
	
	# Basic formatting, prints the data calculated above
	print("Audio Segment Details")
	print("\t Duration (seconds): {}".format(audio_duration))
	print("\t Length (bytes): {}".format(sample_length))
	print("\t Channels: {}".format(channel_count))
	print("\t Max Amplitude: {}".format(max_amplitude))
	print("\t Raw Data Sample: {}".format(raw_data_sample))
	print("\t Raw Data Type: {}".format(raw_data_type))

def AudioSegment_raw(AS_object):
	"""
	Description: Wrapper function for returning the raw data of an Audio Segment object
	Context: Simple way to error check and provide the raw data array associated with an Audio Segment
	Parameters:
		{AS_object} AudioSegment : AudioSegment object
	Return:
		bytestring : Raw data of the audio file is represented as a byte string
	"""

	# Verify the correct object type is passed
	if not AudioSegment_verify(AS_object):
		raise Exception("Provided invalid file type")

	return AS_object.raw_data

def AudioSegment_verify(input):
	"""
	Description: Verifies that the provided parameter is an AudioSegment object
	Context: 
	Parameters:
		{input} Object : Object to be comapred with the AudioSegment class
	Return:
		Boolean : returns True if the provided object is of the AudioSegment class (or subclass)
	"""

	# If the input is the correct type, return True
	if isinstance(input, AudioSegment):
		return True

	return False

AS = dataLoader.load_MP3("CAG.mp3")
AudioSegment_details(AS)
