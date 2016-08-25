from Formant_pyHook_adapt import hook_setup
from Formant_pyHook_adapt import hook_takedown
import sys
import time
import datetime
import msvcrt
import winsound
import pyaudio
import wave
import random
from random import randrange, uniform, shuffle

def get_play_array(num_goals,num_trials):
	playList = []
	print num_trials/num_goals
	if num_goals == 3:
		for i in range(num_trials/num_goals):
			playList.append(1)
		for j in range(num_trials/num_goals):
			playList.append(2)
		for k in range(num_trials/num_goals):
			playList.append(3)
	if num_goals == 5:
		for i in range(num_trials/num_goals):
			playList.append(1)
		for j in range(num_trials/num_goals):
			playList.append(2)
		for k in range(num_trials/num_goals):
			playList.append(3)
		for m in range(num_trials/num_goals):
			playList.append(4)
		for n in range(num_trials/num_goals):
			playList.append(5)	
	random.shuffle(playList)
	print playList
	return playList

def play_goal(playList, playList_place):
	##select a trial from a randomly generated array
	#goal_cue_num = randrange(1,(num_goals+1))
	print playList
	goal_cue_num = playList[playList_place]
	#unfortunately, currently using an if statement so goal cue number has to be hard-coded
	#it seems that python doesn't have a switch statement, the bastards
	
	#Open logfile to write to
	text_file = open('Logfile.txt', 'a')
	
	cur_time = datetime.datetime.now()
	
	#Play the corresponding goal cue
	if goal_cue_num == 1:
		print("Playing goal 1")
		winsound.PlaySound('AH_702_1089_600ms_vol6.wav',winsound.SND_FILENAME)
		text_file.write("At time %d:%d:%d:%d, goal cue F2:1089 F1:702 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))
	elif goal_cue_num == 2:
		print("Playing goal 2")
		winsound.PlaySound('EH_551_1763_600ms_vol6.wav',winsound.SND_FILENAME)
		text_file.write("At time %d:%d:%d:%d, goal cue F2:1763 F1:551 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))
	elif goal_cue_num == 3:
		print("Playing goal 3")
		winsound.PlaySound('EE_294_2254_600ms_vol6.wav',winsound.SND_FILENAME)	
		text_file.write("At time %d:%d:%d:%d, goal cue F2:2254 F1:294 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))
	elif goal_cue_num == 4:
		print("Playing goal 4")
		winsound.PlaySound('UH_450_1030_600ms_vol6.wav',winsound.SND_FILENAME)	
		text_file.write("At time %d:%d:%d:%d, goal cue F2:1030 F1:450 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))
	elif goal_cue_num == 5:
		print("Playing goal 5")
		winsound.PlaySound('AY_400_1917_600ms_vol6.wav',winsound.SND_FILENAME)	
		text_file.write("At time %d:%d:%d:%d, goal cue F2:1917 F1:400 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))

	text_file.close()
	
def jitter():
	#time increment between 0 and 300 milliseconds intended to prevent predictability
	jitter_time = uniform(0,.3)
	time.sleep(jitter_time)

def hook_warmup():
	#intending to run the hook a few times to get it warmed up, as it seems to have a lag for the first few trials
	for increment in range (0,3):
		print("Press for warmup cue")
		temphook = hook_setup(3)
		time.sleep(.6)
		
	print("Press any key to continue")
	msvcrt.getch()
	time.sleep(5)
	return temphook
	
def train_session(num_goals,train_trials):
	#Come up with a randomized array of goals to playList
	playList = get_play_array(num_goals,train_trials)
	
	#Running all of the training trials
	for cur_train_trial in range(0,train_trials):
			
		play_goal(playList,cur_train_trial)
		
		#call hook to wait for any response
		hm = hook_setup(1)
		time.sleep(.6) #Time for the response to finish playing
		
		#now wait for reset cue, they will indicate they are ready to continue by pressing the lower-right-hand corner of the screen
		#hm_continue = hook_setup_continue()
		hm = hook_setup(2)
		#Still having the problem where it's possible to hit the reset cue twice
		time.sleep(.6)
		
		#600 ms to distinguish reset from target
		time.sleep(.6)
			
		#Jitter time to prevent it from being too reliable
		jitter()	

	
def test_session(num_goals,test_trials):
	#Silent (but still recorded) test session to give open loop trials to see the extent of learning

	#Come up with a randomized array of goals to playList
	playList = get_play_array(num_goals,test_trials)
	
	#Running all of the training trials
	for cur_test_trial in range(0,test_trials):
			
		play_goal(playList,cur_test_trial)
		
		#call hook to wait for any response
		hm = hook_setup(4)
		time.sleep(.6) #Time for the response to finish playing
		
		#now wait for reset cue, they will indicate they are ready to continue by pressing the lower-right-hand corner of the screen
		#hm_continue = hook_setup_continue()
		hm = hook_setup(2)
		#Still having the problem where it's possible to hit the reset cue twice
		time.sleep(.6)
		
		#600 ms to distinguish reset from target
		time.sleep(.6)
			
		#Jitter time to prevent it from being too reliable
		jitter()		
		
		
def rampup_session(num_goals,ramp_trials):
	#Silent (but still recorded) test session to give open loop trials to see the extent of learning
	
	#Come up with a randomized array of goals to playList
	playList = get_play_array(num_goals,ramp_trials)
	
	#Running all of the training trials
	for cur_ramp_trial in range(0,ramp_trials):
			
		play_goal(playList,cur_ramp_trial)
		
		#call hook to wait for any response
		hm = hook_setup(5)
		time.sleep(.6) #Time for the response to finish playing
		
		#now wait for reset cue, they will indicate they are ready to continue by pressing the lower-right-hand corner of the screen
		hm = hook_setup(2)
		#Still having the problem where it's possible to hit the reset cue twice
		time.sleep(.6)
		
		#600 ms to distinguish reset from target
		time.sleep(.6)
			
		#Jitter time to prevent it from being too reliable
		jitter()		
		
def rampdown_session(num_goals,ramp_trials):

	#Come up with a randomized array of goals to playList
	playList = get_play_array(num_goals,ramp_trials)

	#Running all of the training trials
	for cur_ramp_trial in range(0,ramp_trials):
			
		play_goal(num_goals,cur_ramp_trial)
		
		#call hook to wait for any response
		hm = hook_setup(7)
		time.sleep(.6) #Time for the response to finish playing
		
		#now wait for reset cue, they will indicate they are ready to continue by pressing the lower-right-hand corner of the screen
		hm = hook_setup(2)
		#Still having the problem where it's possible to hit the reset cue twice
		time.sleep(.6)
		
		#600 ms to distinguish reset from target
		time.sleep(.6)
			
		#Jitter time to prevent it from being too reliable
		jitter()				
		
		
def adapt_session(num_goals,adapt_trials):

	#Come up with a randomized array of goals to playList
	playList = get_play_array(num_goals,adapt_trials)

	#Running all of the training trials
	for cur_adapt_trial in range(0,adapt_trials):
		
		play_goal(num_goals,cur_adapt_trial)
		
		play_goal(num_goals)
		
		#call hook to wait for any response
		hm = hook_setup(6)
		time.sleep(.6) #Time for the response to finish playing
		
		#now wait for reset cue, they will indicate they are ready to continue by pressing the lower-right-hand corner of the screen
		hm = hook_setup(2)
		#Still having the problem where it's possible to hit the reset cue twice
		time.sleep(.6)
		
		#600 ms to distinguish reset from target
		time.sleep(.6)
			
		#Jitter time to prevent it from being too reliable
		jitter()