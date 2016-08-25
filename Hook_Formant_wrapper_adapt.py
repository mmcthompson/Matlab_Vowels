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


full_trial_blocks = 2 #Should be 2, may be shortened for testing purposes
	
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
	
def get_goal_increments():
	#Determine if you want all of the cues from the beginning or added per each block
	increment_num = 0
	while (increment_num<1) or (increment_num>3):
		sys.stdout.write("Press 1 if you would like the cues to be incremented, 2 if you want them to appear all at once")
		line = sys.stdin.readline()
		if not line:
			#terminate on end of input
			break
		args = line.strip().split()
		if not args:
			#ignore empty lines
			continue
		increment_num = int(args[0])

	return increment_num
	
		
	
if __name__== '__main__':
	#Start off by calling the hook a few times to get rid of the lag at the beginning
	hm_temp = hook_warmup()
	
	#Run a test block
	test_session(3,25)
	
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
	
	#Get ready to start adapting
	train_session(3,30)
	
	#Start the adaptation ramping up
	rampup_session(3,30)
	
	#Hold the adapted formants
	adapt_session(3,60)
	
	#Wait for key press for next trial block to continue
	print("Press any key to continue")
	msvcrt.getch()
	#Give me 5 seconds to switch back to the waiting screen
	time.sleep(5)
	
	#Play the held adapted formants
	adapt_session(3,24)
	
	#Short test block
	test_session(3,5)
	
	#Play the held adapted formants
	adapt_session(3,24)
	
	#Short test block
	test_session(3,5)
	
	#Play the held adapted formants
	adapt_session(3,12)
	
	#begin to ramp down
	rampdown_session(3,12)
	
	#Short test block
	test_session(3,5)
	
	#continue to ramp down
	rampdown_session(3,18)
	
	#return to baseline
	train_session(3,6)
	
	#Short test block
	test_session(3,5)
	
	#Last baseline sessions
	train_session(3,24)
	
	#Last short test_session
	test_session(3,5)
	