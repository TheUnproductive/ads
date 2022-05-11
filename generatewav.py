from fileinput import filename
import wavio
import numpy as np
import argparse
import header as hd


parser = argparse.ArgumentParser(description="Start DoorPi with certain options")
parser.add_argument("-r", action="store", dest='rate', type=int, default=44100,
	help="Set sampling rate")	# samples per second, every second 44100 samples are used, for 100ms --> 44100/(1000/100)
parser.add_argument("-n", action="store", dest='name', type=str, default="h",
    help="Manually configure filename")
parser.add_argument("-d", action="store", dest="data", type=str,
    help="Input data to transform")
parser.add_argument("-f1", action="store", dest="f1", type=float, default=2.0,
    help="Input low bit frequency")
parser.add_argument("-f2", action="store", dest="f2", type=float, default=22048.0,
    help="Input high bit frequency")
parser.add_argument("-head", action="store", dest="header", type=str, default="standard", 
	help="Choose which header to use")
parser.add_argument("-t", action="store", dest="type", type=str, default="txt",
    help="Define the filetype to put in the custom header")
args = parser.parse_args()

head = args.header
rate = args.rate
filename = args.name
file = args.type

T = 1         				# sample duration for each bit (seconds), can be changed using the ms down below
f1 = args.f1   				# sound frequency (Hz) for 0 bit
f2 = args.f2   				# sound frequency (Hz) for 1 bit
start_sequence = 1.0   		# start frequencies
stop_sequence = 22050.0    	# stop frequency
breaker_freq = 4.0			# breaker frequency


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
#------------------------------------------------------------------------------
# start sequence with start_sequence frequency
hd.start(T, rate, x, start_sequence, samples)

if head == "standard":
	hd.standard(T, rate, x, f1, f2, samples)						# set up header
	hd.start(T, rate, x, start_sequence, samples)					# end header with start_sequence
elif head == "short":
	hd.short(T, rate, x, f1, f2, samples)							# set up header
	hd.start(T, rate, x, start_sequence, samples)					# end header with start_sequence
elif head == "custom":
	hd.custom(T, rate, x, f1, f2, file, samples, ms, breaker_freq)	# set up header
	hd.start(T, rate, x, start_sequence, samples)					# end header with start_sequence

# transform bitstream to corresponding frequency 
for i in binout:
	t = np.linspace(0, T, T*rate, endpoint=False)
	if i == '0':
		x.append(np.sin(2*np.pi * f1 * t[:samples]))
	if i == '1':
		x.append(np.sin(2*np.pi * f2 * t[:samples]))


# end sequence with stop_sequence frequency
hd.stop(T, rate, x, stop_sequence, samples)
#------------------------------------------------------------------------------

for i in x:
	for j in i:
		l.append(j);

l = np.array(l)

wavio.write(filename+".wav", l, rate, sampwidth=2)
