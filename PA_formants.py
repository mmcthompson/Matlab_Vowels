#Practice using PortAudio in python
#The hope is to eventually create a way of creating/handling formants directly in python

import sounddevice as sd
import numpy as np


#Random noises for numpy array
data = np.random.uniform(-1,1,44100)
fs = 44100

sd.play(data, fs)
