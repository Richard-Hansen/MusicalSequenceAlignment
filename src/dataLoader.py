# Import music data and convert to processable format

import os
from pydub import AudioSegment

def load_MP3(file_path):
	"""
	Description: This function will attempt to load an mp3 audio file from the provided {file_path} location. If successful, an AudioSegment object will be returned, otherwise None will be returned
	Context: Before processing a file, we must load the necessary audio data, this function will perform that action
	Parameters:
		{file_path} string : The path to the requested audio file
	Return:
		AudioSegment : Returns an object of type AudioSegment, if the provided file is invalid, returns None isntead
	"""

	# Load mp3 from absolute path at specified location {file_path}
	absolute_path = os.path.abspath(file_path)
	
	# Attempt to load file into AudioSegment
	try:
		mp3_file = AudioSegment.from_mp3(absolute_path)
	except FileNotFoundError:
		mp3_file = None
	except:
		raise Exception("Unknown Error while loading mp3, possibly invalid file")
		return

	# Return AudioSegment object
	return mp3_file
