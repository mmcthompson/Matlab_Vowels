from Formant_pyHook_MEG import hook_setup
from Formant_pyHook_MEG import hook_takedown
import sys
import winsound
import time
from random import randrange, uniform
import msvcrt
import pyaudio
import wave
from record_sample import sample_record
import datetime


trial_blocks = 4 #should be 4, shortened for testing purposes
trials_per_block = 120 #Should be 120, shortened for testing purposes
goal_cues = 3 #Possibly up to 5, currently 3 because Ivry thought 5 would be too many to learn quickly

audio = pyaudio.PyAudio()

def jitter():
	#time increment between 0 and 300 milliseconds intended to prevent predictability
	jitter_time = uniform(0,.3)
	time.sleep(jitter_time)

def play_goal(num_goals):
	#select a trial randomly
	goal_cue_num = randrange(1,(num_goals+1))
	#unfortunately, currently useing an if statement so goal cue number has to be hard-coded
	#it seems that python doesn't have a switch statement, the bastards
	
	#Open logfile to write to
	text_file = open('Logfile.txt', 'a')
	
	cur_time = datetime.datetime.now()
	
	#Play the corresponding goal cue
	if goal_cue_num == 1:
		print("Playing goal 1")
		winsound.PlaySound('AH_702_1089_600ms_vol6_left.wav',winsound.SND_FILENAME)
		text_file.write("At time %d:%d:%d:%d, goal cue x:1089 y:702 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))
	elif goal_cue_num == 2:
		print("Playing goal 2")
		winsound.PlaySound('EH_551_1763_600ms_vol6_left.wav',winsound.SND_FILENAME)
		text_file.write("At time %d:%d:%d:%d, goal cue x:1763 y:551 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))
	elif goal_cue_num == 3:
		print("Playing goal 3")
		winsound.PlaySound('EE_294_2254_600ms_vol6_left.wav',winsound.SND_FILENAME)	
		text_file.write("At time %d:%d:%d:%d, goal cue x:2254 y:294 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))
	elif goal_cue_num == 4:
		print("Playing goal 4")
		winsound.PlaySound('UH_450_1030_600ms_vol6.wav',winsound.SND_FILENAME)	
		text_file.write("At time %d:%d:%d:%d, goal cue x:1030 y:450 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))
	elif goal_cue_num == 5:
		print("Playing goal 5")
		winsound.PlaySound('AY_400_1917_600ms_vol6.wav',winsound.SND_FILENAME)	
		text_file.write("At time %d:%d:%d:%d, goal cue x:1917 y:400 was played.\n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond))

	text_file.close()
		
		
#Trying to set up a callback that will allow us to record while doing other things		
#def callback(in_data, frame_count, time_info, status):
	#data = stream.read(1024)
	#return (data, pyaudio.paContinue)
	#global sofar
	#sofar += len(in_data)
	#if numpy:
	#	f = numpy.fromstring(in_data, dtype=numpy.int16)
	#	sys.stderr.write('length %6d sofar %6d std %4.1f \r' \(len(in_data), sofar, numpy.std(f)))
	#else:
	#	sys.stderr.write('length %6d sofar %6d \r' % \ (len(in_data), sofar))
	#	data = None
	#	return (data, pyaudio.paContinue)
	
	
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
	
if __name__== '__main__':

	fs = 44100 #A fairly standard frames per second
	duration = 600 #ten minutes should be more than enough time for even a slow block
				   #(Typically ~6 minutes per block)

	frames = []
	
	#It's going to ask how many goal cues you want
	num_goals = get_num_goals()
	
	#Figure out whether to increment the cues or to play them all at once
	if num_goals > 3:
		increment_num = get_goal_increments()
	else:
		increment_num = 2 #Cues will not be incremented
	
	#Start off by calling the hook a few times to get rid of the lag at the beginning
	hm_temp = hook_warmup()
	
	for cur_block in range (0,trial_blocks):
		#Calling the hook once per trial in trial block
		
		#incrementing the number of goal cues if neccesary
		if increment_num == 2:
			num_cur_goals = num_goals
		elif increment_num == 1:
			if cur_block == 0:
				num_cur_goals = 3
			elif cur_block == 1:
				num_cur_goals = 4
			if (num_goals == 5) and (cur_block == 2):
				num_cur_goals = 5
		
		#if cur_block == (trial_blocks-1):
			#Start the recording, we want to record everything in this block 
			#print ("current block is %i" %cur_block)
			#The chanel we want to record is chanel 4, the speakers chanel
			#ideally, I will be able to start and stop at the beginning and the end of the last trial block
			#for now, we're just going to have to try to settle for a fixed period of time that will be long enough to get everything			
			#listen_condition = sd.rec(duration * fs, samplerate=fs, channels=1, mapping=4)
			
			#attempting to start a portaudio (equivalent) stream
			#stream = audio.open(format=pyaudio.paInt16, channels=2, rate=fs, input=True, frames_per_buffer=1024)
			#frames = []

			#Trying the new callback method
			#stream = audio.open(format=pyaudio.paInt16, channels=2, rate=fs, input=True, stream_callback=callback)
			#stream.start_stream()
			
			#in theory this should record for a set amount of time without interfering with the loop
			#sample_record()
		
		for cur_trial in range(0,trials_per_block):
		
			#winsound.PlaySound('Break_cue_right2.wav',winsound.SND_FILENAME)
		
			#Attempting to start recording if it's start of the listen block
			#if cur_block == (trial_blocks-1):
			#	data = stream.read(1024)
			#	frames.append(data)
			
			play_goal(num_cur_goals)
			#time.sleep(.6) #Goal cue length, time for goal cue to play before hook is activated
		
			#appears a little slow. Check when finalized to see if it is too, problematically slow 
			#call hook to wait for any response
			hm = hook_setup(1)
			time.sleep(.6) #Time for the response to finish playing
		
			#print("Completed hook for this round")
			#Half a second to distinguish the response from the next cue
			#time.sleep(1)
			
			#now wait for reset cue, they will indicate they are ready to continue by pressing the lower-right-hand corner of the screen
			#hm_continue = hook_setup_continue()
			hm = hook_setup(2)
			time.sleep(.3)
		
			#600 ms to distinguish reset from target
			time.sleep(.6)
			
			#Jitter time to prevent it from being too reliable
			jitter()
			
			
		#Wait for key press for next trial block to continue
		#Making sure to catch the last trial 
		#if cur_block == (trial_blocks-1):
		#	data = stream.read(1024)
		#	frames.append(data)
		print("Press any key to continue")
		msvcrt.getch()
		#Give me 5 seconds to switch back to the waiting screen
		time.sleep(5)
	
	#stop recording 
	#stream.stop_stream()
	#stream.close()
	#audio.terminate()
	#sd.stop()
	#sd.play(listen_condition, fs)
	
	##Write to and play .wav file you have created of the recording
	waveFile = wave.open("recording.wav", 'wb')
	waveFile.setnchannels(2)
	waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
	waveFile.setframerate(fs)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
	
	print("playing .wav file")
	
	winsound.PlaySound('recording.wav',winsound.SND_FILENAME)

	print("done playing .wav file")
	
	#shut down the hook(s)
	#hook_takedown(hm)
	#hook_takedown(hm_continue)
	#hook_takedown(hm_temp)