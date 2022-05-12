## This is a WIP file

import wavio
import numpy as np
import argparse
from pydub import AudioSegment
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.fftpack
import scipy
import os

parser = argparse.ArgumentParser(description="Decrypt wav file")	
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

print(output)

for i, chunk in enumerate(in_data[::ms]):
  with open("sounds/sound-%s.wav" % i, "wb") as f:
    chunk.export(f, format="wav")

files = os.listdir("sounds")
for i in files:
    filename = "sounds/" + i
    fs_rate, signal = wavfile.read(filename)

    print ("Frequency sampling", fs_rate)
    l_audio = len(signal.shape)
    print ("Channels", l_audio)
    if l_audio == 2:
        signal = signal.sum(axis=1) / 2
    N = signal.shape[0]
    print ("Complete Samplings N", N)
    secs = N / float(fs_rate)
    print ("secs", secs)
    Ts = 1.0/fs_rate # sampling interval in time
    print ("Timestep between samples Ts", Ts)
    t = np.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray
    FFT = scipy.fftpack.fft(signal)
    FFT = abs(FFT)
    FFT_side = FFT[range(N//2)] # one side FFT range
    freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
    fft_freqs = np.array(freqs)
    freqs_side = freqs[range(N//2)] # one side frequency range
    fft_freqs_side = np.array(freqs_side)
    print(np.argmax(abs(FFT_side)))# plotting the positive fft spectrum

    os.system("rm " + filename)