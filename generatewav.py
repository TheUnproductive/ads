from fileinput import filename
import wavio
import numpy as np
import argparse
import header as hd
from pydub import AudioSegment

def combine(input_file, inject_file, output_file):
	sound1 = AudioSegment.from_file(input_file)
	inject_raw = AudioSegment.from_file(inject_file)
	sound2 = inject_raw - 55
	combined = sound1.overlay(sound2)
	combined.export(output_file, format='wav')

parser = argparse.ArgumentParser(description="Encrypt wav file")
parser.add_argument("-r", action="store", dest='rate', type=int, default=48000,
	help="Set sampling rate")	# samples per second, every second 44100 samples are used, for 100ms --> 44100/(1000/100)
parser.add_argument("-d", action="store", dest="data", type=str,
    help="Input data to transform")
parser.add_argument("-f1", action="store", dest="f1", type=float, default=22000.0,
    help="Input low bit frequency")
parser.add_argument("-f2", action="store", dest="f2", type=float, default=23000.0,
    help="Input high bit frequency")
parser.add_argument("-head", action="store", dest="header", type=str, default="standard", 
	help="Choose which header to use")
parser.add_argument("-t", action="store", dest="type", type=str, default="txt",
    help="Define the filetype to put in the custom header")
parser.add_argument("-in", action="store", dest="input", type=str)
parser.add_argument("-out", action="store", dest="output", type=str, default="h.wav")
args = parser.parse_args()

head = args.header
rate = args.rate
file = args.type

T = 1         				# sample duration for each bit (seconds), can be changed using the ms down below
f1 = args.f1   				# sound frequency (Hz) for 0 bit
f2 = args.f2   				# sound frequency (Hz) for 1 bit


ms = 5; #milliseconds between each bit
samples = rate//(1000//ms)

if f1 > rate//2 or f2 > rate//2:
	print("Error, maximum frequency exceeds " + str(rate/2))
	exit()

if args.data:
	s = args.data
else:
	s = input("Enter your data: ")

x = []
l = []

#------------------------------------------------------------------------------
if args.data:
	if file == "txt":
		s = open(s, "r")
		string_s = ""
		for line in s:
			string_s = string_s + line
		s = string_s


print("Input Stream: " + (''.join(map(bin,bytearray(s, 'utf-8')))) + "\n")
binout = ((''.join(map(bin,bytearray(s, 'utf-8')))).replace("b", "")).replace(" ", "")
print("Binout: %s \n" % (binout))
file_len = len(binout)
#------------------------------------------------------------------------------
# start sequence with start_sequence frequency

if head == "standard":
	header_bits = len(bin(ms)) + len(bin(file_len))
	print(header_bits)
	hd.writeheaderdata_padded(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), header_bits)
	hd.standard(T, rate, x, f1, f2, samples, ms, file_len)						# set up header
elif head == "short":
	header_bits = len(bin(ms)) + len(bin(file_len))
	hd.writeheaderdata(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), str(header_bits))
	hd.short(T, rate, x, f1, f2, samples)							# set up header
elif head == "custom":
	header_bits = len(bin(int(f1))) + len(bin(int(f2))) + len(bin(rate)) + len(bin(ms)) + len(bin(file_len))
	print(header_bits)
	hd.writeheaderdata(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), str(header_bits))
	hd.custom(T, rate, x, f1, f2, file, samples, ms, file_len)	# set up header

# transform bitstream to corresponding frequency 
for i in binout:
	t = np.linspace(0, T, T*rate, endpoint=False)
	if i == '0':
		x.append(np.sin(2*np.pi * f1 * t[:samples]))
	if i == '1':
		x.append(np.sin(2*np.pi * f2 * t[:samples]))

#------------------------------------------------------------------------------

for i in x:
	for j in i:
		l.append(j);

l = np.array(l)

if args.input:
	wavio.write(args.output, l, rate, sampwidth=2)
	combine(args.input, args.output, args.output)
else:
	wavio.write(args.output, l, rate, sampwidth=2)