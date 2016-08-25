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

#upper left is really lower left
#no targets announced
#the labels are obnoxious
#Reset tone is too long/sensitive again
#You didn't give them dummy F1 and F2 values
#problems with the floats for the inputs. Working on it, try again.
#Also, upper left is 0,0


def onlowerright(event):

	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) >= (2*1920/3)) and ((pos[1]) >= (3*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		#winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		#Pass formants into shorter-cued matlab program
		eng.formant_synthesize_playback_300ms_1000hz_tone(float(0),float(0),nargout=0)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True

def onupperright(event):

	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) >= (2*1920/3)) and ((pos[1]) <= (1*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		#winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		#Pass formants into shorter-cued matlab program
		eng.formant_synthesize_playback_300ms_1000hz_tone(float(0),float(0),nargout=0)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True

def onupperleft(event):

	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) <= (1*1920/3)) and ((pos[1]) <= (1*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
#		winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		#Pass formants into shorter-cued matlab program
		eng.formant_synthesize_playback_300ms_1000hz_tone(float(0),float(0),nargout=0)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")
	
	return True

def onlowerleft(event):

	pos = event.Position
	print(pos)
	
	#Input limited to upper 1/12 of the screen. Otherwise, loop essentially continues
	if ((pos[0]) <= (1*1920/3)) and ((pos[1]) >= (3*1080/4)):
		#Click is in lower-right-hand corner, allow to proceed 
		#winsound.PlaySound('Break_cue_right.wav',winsound.SND_FILENAME)
		#Pass formants into shorter-cued matlab program
		eng.formant_synthesize_playback_300ms_1000hz_tone(float(0),float(0),nargout=0)
		
		#Break after one input in the correct area
		ctypes.windll.user32.PostQuitMessage(0)
		#print (pos)
	else:
		print ("incorrect reset")

	return True	
	
	
def hook_setup_upperleft():
	print("Setting up the test")
	
	#Create hook manager
	hm = pyHook.HookManager()
		
	hm.MouseAll = onupperleft
	
	#Set the hook
	hm.HookMouse()
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm.HookKeyboard()
	
	pythoncom.PumpMessages()

	hm.UnhookMouse()
	hm.UnhookKeyboard()
	return hm

def hook_setup_upperright():
	#setting up the hook only to catch the reset cue indicating the subject is ready for the next trial
	print("Setting up the test")
	
	#Create hook manager
	hm = pyHook.HookManager()
		
	#play the alternate oncluc which only accepts lower-right-hand reset presses
	hm.MouseAll = onupperright
	
	#Set the hook
	hm.HookMouse()
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm.HookKeyboard()
	
	pythoncom.PumpMessages()

	hm.UnhookMouse()
	hm.UnhookKeyboard()
	return hm
	
def hook_setup_lowerleft():
	#setting up the hook only to catch the reset cue indicating the subject is ready for the next trial
	print("Setting up the test")
	
	#Create hook manager
	hm = pyHook.HookManager()
	
	#play the alternate oncluc which only accepts lower-right-hand reset presses
	hm.MouseAll = onlowerleft
	
	#Set the hook
	hm.HookMouse()
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm.HookKeyboard()
	
	pythoncom.PumpMessages()

	hm.UnhookMouse()
	hm.UnhookKeyboard()
	return hm

def hook_setup_lowerright():
	#setting up the hook only to catch the reset cue indicating the subject is ready for the next trial
	print("Setting up the test")
	
	#Create hook manager
	hm = pyHook.HookManager()
	
	#play the alternate oncluc which only accepts lower-right-hand reset presses
	hm.MouseAll = onlowerright
	
	#Set the hook
	hm.HookMouse()
	
	
	#Set the keyboard hook (that doesn't have a callback so I'm never going to use it) because otherwise it whines at me
	hm.HookKeyboard()
	
	pythoncom.PumpMessages()
	
	hm.UnhookMouse()
	hm.UnhookKeyboard()
	return hm


	
if __name__== '__main__':
	
	for i in range(1,4):
		winsound.PlaySound('Upper_Left.wav',winsound.SND_FILENAME)
		print("requesting upper left")
		hook_setup_upperleft()
		#Give it a chance to breathe before the next target is announced
		time.sleep(1)
		
		winsound.PlaySound('Upper_Right.wav',winsound.SND_FILENAME)
		print("requesting upper right")
		hook_setup_upperright()
		time.sleep(1)
		
		winsound.PlaySound('Lower_Left.wav',winsound.SND_FILENAME)
		print("requesting lower left")
		hook_setup_lowerleft()
		time.sleep(1)
		
		winsound.PlaySound('Lower_Right.wav',winsound.SND_FILENAME)
		print("requesting lower right")
		hook_setup_lowerright()
		time.sleep(1)
	
time.sleep(3)
