## This is a WIP file

import wavio
import numpy as np
import argparse
from scipy.io import wavfile
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Start DoorPi with certain options")
parser.add_argument("-r", action="store", dest='rate', type=int, default=44100,
	help="Set sampling rate")	# samples per second, every second 44100 samples are used, for 100ms --> 44100/(1000/100)
parser.add_argument("-n", action="store", dest='name', type=str, default="h",
    help="Manually configure filename")
parser.add_argument("-d", action="store", dest="data", type=str,
    help="Input data to transform")
args = parser.parse_args()

rate = args.rate
filename = args.name

T = 1         # sample duration for each bit (seconds), can be changed using the ms down below
f1 = 1200.0   # sound frequency (Hz) for 0 bit
f2 = 44000.0   # sound frequency (Hz) for 1 bit
start_sequence = 1800.0   # start frequencies
stop_sequence = 3600.0    # stop frequency


ms = 10; #milliseconds between each bit
samples = rate//(1000//ms)

if f1 > rate//2 or f2 > rate//2:
	print("Error, maximum frequency exceeds " + str(rate/2))
	exit()

if args.data:
	s = args.data
else:
	s = input("Enter your data: ")
	s += '.'

print("Input Stream: " + (''.join(map(bin,bytearray(s, 'utf-8')))) + "\n")
binout = ((''.join(map(bin,bytearray(s, 'utf-8')))).replace("b", "")).replace(" ", "")
print("Binout: %s \n" % (binout))

x = []
l = []

def openWavFile(filename):
    sampling_rate, data = wavfile.read(filename)
    print(f"sampling rate: {sampling_rate}")

    length = data.shape[0] / sampling_rate
    print(f"length = {length}s")
    
    return sampling_rate, data

def extract_peak_frequency(data, sampling_rate):
    fft_data = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(data))
    
    peak_coefficient = np.argmax(np.abs(fft_data))
    peak_freq = freqs[peak_coefficient]
    
    return abs(peak_freq * sampling_rate)

def getChunks(milliseconds, sampling_rate):
    #divide this extracted data into 50ms chunks, and find the peak or dominant frequency of each chunk
    #now if the chunk's peak frequency is 1200Hz, then it is 0 bit and if it's 1400Hz, then it is 1 bit.
    #group these bits together and that's the received data
    try:
        milliseconds = milliseconds/1000

        delay = int(milliseconds*sampling_rate)
        print(f"delay between tones: {delay} samples")
        chunks = []

        data_length = len(data) - len(data)%delay
        prev = 0

        for i in range(delay, data_length, delay):
            chunks.append(data[prev:i])
            prev = i
    except:
        pass
    
    
    return chunks

def extractData(chunks, sampling_rate):
    try:
        peak_freqs = []
        for chunk in chunks:
            peak_freqs.append(round(extract_peak_frequency(chunk, sampling_rate), 0))
    except:
        pass
    
    return peak_freqs

def extractBits(peak_freqs):
    bits = []
    foundStartSequence = False
    foundEndSequence = False
    for frequency in peak_freqs:
        if(frequency >= 2495 and frequency <= 2505 and foundStartSequence == False):
            foundStartSequence = True
            print("Start sequence found!")
        
        elif(frequency >= 3495 and frequency <= 3505 and foundEndSequence == False):
            foundEndSequence = True
            print("End sequence found!")
            break
        
        elif(frequency >= freq1-10.0 and frequency <= freq1+10.0):
            bits.append(0)
        
        elif(frequency >= freq2-10.0 and frequency <= freq2+10.0):
            bits.append(1)
            
    bin_bits = []
    s = ""
    for i in range(len(bits)):
        if (i+1)%8 == 0:
            s += str(bits[i])
            bin_bits.append(s)
            s = ""
        else:
            s += str(bits[i])
            
    return bin_bits

def decodeAscii(bin_string):
    """binary_int = int(bin_string, 2);
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = "Bin string cannot be decoded"
    for enc in ['utf-8', 'ascii', 'ansi']:
        try:
            ascii_text = binary_array.decode(encoding=enc)
            break
        except:
            pass
    print(ascii_text)"""
    
    
    bin_to_str = "".join([chr(int(bin_string[i:i+8],2)) for i in range(0,len(bin_string),8)])

    return bin_to_str