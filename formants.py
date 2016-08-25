#formants.py courtesy of GitHub user danilobellini
#Can be found on: https://github.com/danilobellini/audiolazy/blob/master/examples/formants.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of AudioLazy, the signal processing Python package.
# Copyright (C) 2012-2014 Danilo de Jesus da Silva Bellini
#
# AudioLazy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Created on Tue Sep 10 18:02:32 2013
# danilo [dot] bellini [at] gmail [dot] com
"""
Voiced "ah-eh-ee-oh-oo" based on resonators at formant frequencies
"""

from __future__ import unicode_literals, print_function

from audiolazy import (sHz, maverage, rint, AudioIO, ControlStream,
                       CascadeFilter, resonator, saw_table, chunks)
from time import sleep
import sys

# Script input, change this with symbols from the table below
vowels = "e"

# Formant table from in http://en.wikipedia.org/wiki/Formant
formants = {
  "i": [240, 2400],
  "y": [235, 2100],
  "e": [390, 2300],
  "a": [850, 1610],
  "o": [360, 640],
  "u": [250, 595],
}


# Initialization
rate = 44100
s, Hz = sHz(rate)
inertia_dur = .5 * s
inertia_filter = maverage(rint(inertia_dur))

api = sys.argv[1] if sys.argv[1:] else None # Choose API via command-line
chunks.size = 1 if api == "jack" else 16
print(api)

#AudioIO()

with AudioIO(api) as player:
#with AudioIO() as player:
  first_coeffs = formants[vowels[0]]

  #print(first_coeffs)
  # These are signals to be changed during the synthesis
  f1 = ControlStream(first_coeffs[0] * Hz)
  f2 = ControlStream(first_coeffs[1] * Hz)
  print(f1)
  print(f2)
  gain = ControlStream(0) # For fading in

  # Creates the playing signal
  filt = CascadeFilter([
    resonator.z_exp(inertia_filter(f1).skip(inertia_dur), 400 * Hz),
    resonator.z_exp(inertia_filter(f2).skip(inertia_dur), 2000 * Hz),
  ])
  sig = filt((saw_table)(100 * Hz)) * inertia_filter(gain)

  print(sig.name)
  print(sig.description)
  print(sig)
  th = player.play(sig)
  
  sleep(2)
  for vowel in vowels:
    coeffs = formants[vowel]
    #print(coeffs)
    print("Now playing: ", vowel)
    f1.value = coeffs[0] * Hz
    f2.value = coeffs[1] * Hz
    gain.value = 1 # Fade in the first vowel, changes nothing afterwards
    sleep(2)
#  gain.value = 1
#  sleep(2)



  # Fade out
  gain.value = 0
  sleep(inertia_dur / s + .2) # Divide by s because here it's already
                              # expecting a value in seconds, and we don't
                              # want ot give a value in a time-squaed unit
                              # like s ** 2