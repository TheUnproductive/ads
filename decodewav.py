## This is a WIP file

import numpy as np
import argparse
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.fftpack
import scipy
from scipy import signal
import os
from pydub import AudioSegment

parser = argparse.ArgumentParser(description="Decrypt wav file")	
parser.add_argument("-n", action="store", dest='name', type=str, default="h.wav",
    help="Manually configure filename")
args = parser.parse_args()

rate = 48000    # samples per second, every second 44100 samples are used, for 100ms --> 44100/(1000/100)
filename = args.name

T = 1         # sample duration for each bit (seconds), can be changed using the ms down below
f1 = 22000.0   # sound frequency (Hz) for 0 bit
f2 = 23000.0   # sound frequency (Hz) for 1 bit
start_sequence = 20000.0   # start frequencies
stop_sequence = 20000.0    # stop frequency


ms = 5; #milliseconds between each bit
samples = rate//(1000//ms)

if f1 > rate//2 or f2 > rate//2:
	print("Error, maximum frequency exceeds " + str(rate/2))
	exit()

rate, data = wavfile.read(filename)
# rate=48000, data.shape=(46447, 2) ~ almost 1s of stereo signal

print(rate)
    
f, t, Sxx = signal.spectrogram(data, rate, nperseg=512)  # t starts at 1 ms as index 0

print(Sxx)

plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig("fig.png")
plt.show()