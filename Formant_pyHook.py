import pyHook
import pythoncom
import ctypes
import sys
sys.path.append("C:/Users/Megan/Documents/PhDSecondYear/Touchscreen/Matlab_Vowels")
import matlab.engine
eng = matlab.engine.start_matlab()
import winsound
import time
from random import randrange, uniform
import datetime

#Things you need:
#Python 2.7-3.4
#Matlab 2015 (I think 2014b might also work)
#pyHook for 64-bit windows and python 2.7-3
#Installing all of this will break your heart and spirit. Repeatedly.
#These websites will be useful: 
#http://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html
#http://stackoverflow.com/questions/23362217/error-while-installing-cplex-12-6-for-python
#Also: you need to move PyHook to C:\Python34\Lib\site-packages, and install pythoncom to that folder as well
#Pythoncom can be downloaded as part of pywin32 at https://sourceforge.net/projects/pywin32/files/pywin32/ 


#Steps:
#1. Download and install python2.7 (https://www.python.org/downloads/release/python-2711/)
#2. Add both python27 and python27/Scripts to path (found in settings->system->about->system info->Advanced system settings->environmental variables->edit path)
#3. Download the appropriate pyHook in the form of a .whl file (http://www.lfd.uci.edu/~gohlke/pythonlibs/)
#4. Install pyHook using pip install pyHook-1.5.1-cp27-none-win_amd64.whl
#5. Download and install matlab. Activation key is: 12565-53601-73617-07179-27354
#6. Enable the matlab engine to run in python by following the instructions here:http://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html 
#7. Download pythoncom at https://sourceforge.net/projects/pywin32/files/pywin32/  

#Steps I want for the experiment:
#In trial blocks: 4 blocks of 120 trials
#A randomized (but different) goal cue will be played 
#Potentially 3 goal cues, "EE"(295,2254), "EH"(551,1763), and "AH"(702,1089)
#Note: must shorten period of tone in matlab
#Wait for a response
#Play response
#Log response to text file log, allong with (maybe) calculating error distance



def onclick(event):
	#Open and print to textfile.
	text_file = open('Logfile.txt', 'a')
	print("Classic click detected")
	print(event.Position)
	pos = event.Position

	
	#Input must be shifted based on size of screen (1920x1075) and range of formants we want to 
	
	#old mapping included (0-2500F2, 0-850F1), F2 on the x-axis, F1 on the y-axis	
	#F2_pos = 2500 - 2500*(float(pos[0])/float(1920))
	#F1_pos = 850*(float(pos[1])/float(850))
	
	#new mapping: include (900-2500F2, 300-850F1), F2 on the x-axis, F1 on the y-axis
	#Designed so that "oooooh" is at the bottom-right corner
	#F2_pos = (float(900-2500)/float(1920))*(pos[0]) + 2500
	F2_pos = (float(800-2500)/float(1920))*(pos[0]) + 2500
	#F1_pos = (float(300-850)/float(1080))*(pos[1]) + 850
	#Extending mapping to make F1 300-850Hz so that none of the cues are completely on the bottom of the screen
	F1_pos = (float(100-900)/float(1080))*(pos[1]) + 900
	
	#Pass position into matlab program
	eng.formant_synthesize_playback(float(F1_pos),float(F2_pos),nargout=0)
	#print("Done with classic mouse playback")
	
	#Write time and postition to logfile
	cur_time = datetime.datetime.now()
	text_file.write("At time %d:%d:%d:%d position was x:%d y:%d with resulting formants F2:%f F1:%f \n" %(cur_time.hour, cur_time.minute, cur_time.second, cur_time.microsecond, pos[0], pos[1], F2_pos, F1_pos)) 
	text_file.close()
	
	#Break after one input 
	ctypes.windll.user32.PostQuitMessage(0)
	#print("broken from message pump")
	return True
	
def oncornerclick(event):
	print("corner click detected")
	pos = event.Position
	print(pos)
	
	#Input limited to lower 1/32 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) >= (7*1920/8)) and ((pos[1]) >= (3*1075/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		#F2_pos = ((900-2500)/1920)*(pos[0]) + 2500
		#F1_pos = ((300-850)/1075)*(pos[1]) + 850
		F2_pos = (float(800-2500)/float(1920))*(pos[0]) + 2500
		F1_pos = (float(100-900)/float(1080))*(pos[1]) + 900
		
		
		#Pass formants into shorter-cued matlab program
		eng.formant_synthesize_playback_3ms_tone(float(F1_pos),float(F2_pos),nargout=0)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True
	
def onwarmup(event):
	print("warmup click detected")
	pos = event.Position
	
	#input isn't really important, this is a silent cue
	fake_F1 = 400
	fake_F2 = 400
	
	#pass unimportant inputs into silent matlab program
	#eng.formant_synthesize_silence(float(fake_F1),float(fake_F2),nargout=0)
	eng.formant_synthesize_playback(float(fake_F1),float(fake_F2),nargout=0)
	
	ctypes.windll.user32.PostQuitMessage(0)
	return True
	
	
#def onkey(event):
#	print(chr(event.Ascii))
#	#print(event.Ascii)
#	if chr(event.Ascii) == 'q':
#		ctypes.windll.user32.PostQuitMessage(0)	
#	#keepflag = False
#	return True

#Set up as a function so it can be called in loop in other function/script
def hook_setup(condition):

	#print ("setting up hook")
	#Create hook manager
	hm = pyHook.HookManager()

	#If this is a standard response, we're going to want to watch for all mouse events
	if condition == 1:
		#Watch for all mouse events
		print("calling the classic click")
		hm.MouseAll = onclick
	elif condition == 2:
		print("calling the corner click")
		#watch for only mouse events in the lower right-hand corner 
		hm.MouseAll = oncornerclick
	elif condition == 3:
		print("calling the warmup click")
		#play a silent cue to help attenuate delay
		hm.MouseAll = onwarmup
	
	#Set the hook
	hm.HookMouse()

#	#Watch for all keyboard events
#	hm.KeyDown = onkey
#	#Set the hook
	hm.HookKeyboard()

	#Only seems to take too long when run through cygwin, not PowerShell
	pythoncom.PumpMessages()
	
	hm.UnhookMouse()
	hm.UnhookKeyboard()
	return hm
	
def hook_setup_continue():
	#setting up the hook only to catch the reset cue indicating the subject is ready for the next trial
	print("Setting up the continue")
	
	#Create hook manager
	hm2 = pyHook.HookManager()
	
	print("starting corner callback")
	
	#play the alternate oncluc which only accepts lower-right-hand reset presses
	hm2.MouseAll = oncornerclick
	
	#Set the hook
	hm2.HookMouse()
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm2.HookKeyboard()
	
	pythoncom.PumpMessages()
	return hm2
	
def hook_setup_warmup():
	#This is intended to be a silent hook because shortly after any hook is initiated there is a few-trials delay.
	#This is a quick solution attempting to remedy that problem
	#Create hook manager
	hm = pyHook.HookManager()

	#If this is a standard response, we're going to want to watch for all mouse events
	#Watch for all mouse events
	hm.MouseAll = onwarmup
	
	#Set the hook
	hm.HookMouse()

#	#Watch for all keyboard events
#	hm.KeyDown = onkey
#	#Set the hook
	hm.HookKeyboard()

	#Only seems to take too long when run through cygwin, not PowerShell
	pythoncom.PumpMessages()
	return hm
	
	
def hook_takedown(hm):
	hm.UnhookMouse()
	hm.UnhookKeyboard()
	#eng.quit()
	