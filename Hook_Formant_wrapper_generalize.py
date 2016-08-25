from Hook_Block_Types import hook_warmup
from Hook_Block_Types import train_session
from Hook_Block_Types import test_session
from Hook_Block_Types import rampup_session
from Hook_Block_Types import rampdown_session
from Hook_Block_Types import adapt_session
from Hook_Block_Types import play_goal
import sys
import winsound
import time
import msvcrt
import pyaudio
import wave
from record_sample import sample_record
import datetime


full_trial_blocks = 3
	
	
def get_num_goals():
	#Determine how many cues you want
	num_cues = 0
	while (num_cues < 1) or (num_cues > 5):
		sys.stdout.write("Please enter how many cues you want to play (1-5):")
		line = sys.stdin.readline()
		if not line:
			#terminate on end of input
			break
		args = line.strip().split()
		if not args:
			#ignore empty lines
			continue
		num_cues = int(args[0])

		
	return num_cues
	
		
	
if __name__== '__main__':
	
	#Start off by calling the hook a few times to get rid of the lag at the beginning
	hm_temp = hook_warmup()
	
	#Run a test block
	test_session(3,24)
	
	#Wait for key press for next trial block to continue
	print("Press any key to continue")
	msvcrt.getch()
	#Give me 5 seconds to switch back to the waiting screen
	time.sleep(5)
		
	for cur_block in range (0,full_trial_blocks):
		#Calling the hook once per trial in trial block
		train_session(3,120)
		
		#Wait for key press for next trial block to continue
		print("Press any key to continue")
		msvcrt.getch()
		#Give me 5 seconds to switch back to the waiting screen
		time.sleep(5)
	
	for cur_short_block in range (0,5):
		#Alternate between training and testing for the final block
		#run a training session
		train_session(3,24)
		
		#run a test session
		test_session(5,5)