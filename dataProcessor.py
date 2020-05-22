# This file provides functionality for processing a provided AudioSegment object into a more useable format, also provides auxillary debugging and information tools

from pydub import AudioSegment
import dataLoader

def AudioSegment_Details(AS_object):
	"""
	Description: This functtion will print general data about the provided AudioSegment file
	Context: When debugging or attempting to modify files, easy access to an info sheet is useful
	Parameters:
		{AS_object} AudioSegment : AudioSegment object
	Return:
		NA
	"""

	# Data we will be displaying
	audio_duration = AS_object.duration_seconds
	channel_count = AS_object.channels
	max_amplitude = AS_object.max
	raw_data_sample = AS_object[0:min(len(AS_object), 5)].raw_data
	
	# Basic formatting
	print("Audio Segment Details")
	print("\t Duration (seconds): {}".format(audio_duration))
	print("\t Channels: {}".format(channel_count))
	print("\t Max Amplitude: {}".format(max_amplitude))
	print("\t Raw Data Sample: {}".format(raw_data_sample))

AS = dataLoader.load_MP3("CAG.mp3")
AudioSegment_Details(AS)