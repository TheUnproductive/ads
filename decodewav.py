## This is a WIP file

import wavio
import numpy as np
import argparse
from pydub import AudioSegment
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.fftpack
import scipy

parser = argparse.ArgumentParser(description="Start DoorPi with certain options")	
parser.add_argument("-n", action="store", dest='name', type=str, default="h.wav",
    help="Manually configure filename")
args = parser.parse_args()

rate = 44100    # samples per second, every second 44100 samples are used, for 100ms --> 44100/(1000/100)
filename = args.name

T = 1         # sample duration for each bit (seconds), can be changed using the ms down below
f1 = 2.0   # sound frequency (Hz) for 0 bit
f2 = 3.0   # sound frequency (Hz) for 1 bit
start_sequence = 1.0   # start frequencies
stop_sequence = 5.0    # stop frequency


ms = 5; #milliseconds between each bit
samples = rate//(1000//ms)

if f1 > rate//2 or f2 > rate//2:
	print("Error, maximum frequency exceeds " + str(rate/2))
	exit()

in_data = AudioSegment.from_file(filename)

output = []

for i, chunk in enumerate(in_data[::ms]):
    output.append(chunk)


peak_amplitude = output[0].get_array_of_samples()
print(peak_amplitude)
