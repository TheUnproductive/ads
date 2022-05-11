## This is a WIP file

import wavio
import numpy as np
import argparse
from scipy.io import wavfile
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Start DoorPi with certain options")
parser.add_argument("-r", action="store", dest='rate', type=int, default=44100,
	help="Set sampling rate")	# samples per second, every second 44100 samples are used, for 100ms --> 44100/(1000/100)
parser.add_argument("-n", action="store", dest='name', type=str, default="h.wav",
    help="Manually configure filename")
parser.add_argument("-d", action="store", dest="data", type=str,
    help="Input data to transform")
args = parser.parse_args()

rate = args.rate
filename = args.name

T = 1         # sample duration for each bit (seconds), can be changed using the ms down below
f1 = 2.0   # sound frequency (Hz) for 0 bit
f2 = 21000.0   # sound frequency (Hz) for 1 bit
start_sequence = 1.0   # start frequencies
stop_sequence = 22000.0    # stop frequency


ms = 5; #milliseconds between each bit
samples = rate//(1000//ms)

if f1 > rate//2 or f2 > rate//2:
	print("Error, maximum frequency exceeds " + str(rate/2))
	exit()

#if args.data:
#	s = args.data
#else:
#	s = input("Enter your data: ")
#	s += '.'

#print("Input Stream: " + (''.join(map(bin,bytearray(s, 'utf-8')))) + "\n")
#binout = ((''.join(map(bin,bytearray(s, 'utf-8')))).replace("b", "")).replace(" ", "")
#print("Binout: %s \n" % (binout))
#
#x = []
#l = []
