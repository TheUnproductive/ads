from fileinput import filename
import wavio
import numpy as np
import argparse


parser = argparse.ArgumentParser(description="Start DoorPi with certain options")
parser.add_argument("-r", action="store", dest='rate', type=int, default=44100,
	help="Set sampling rate")	# samples per second, every second 44100 samples are used, for 100ms --> 44100/(1000/100)
parser.add_argument("-n", action="store", dest='name', type=str, default="h",
    help="Manually configure filename")
parser.add_argument("-d", action="store", dest="data", type=str,
    help="Input data to transform")
parser.add_argument("-f1", action="store", dest="f1", type=float, default=1200.0,
    help="Input low bit frequency")
parser.add_argument("-f2", action="store", dest="f2", type=float, default=2600.0,
    help="Input high bit frequency")
parser.add_argument("-start", action="store", dest="start", type=float, default=1800.0,
    help="Input high bit frequency")
parser.add_argument("-stop", action="store", dest="stop", type=float, default=3600.0,
    help="Input high bit frequency")
args = parser.parse_args()

rate = args.rate
filename = args.name

T = 1         # sample duration for each bit (seconds), can be changed using the ms down below
f1 = args.f1   # sound frequency (Hz) for 0 bit
f2 = args.f2   # sound frequency (Hz) for 1 bit
start_sequence = args.start   # start frequencies
stop_sequence = args.stop    # stop frequency


ms = 5; #milliseconds between each bit
samples = rate//(1000//ms)

if f1 > rate//2 or f2 > rate//2:
	print("Error, maximum frequency exceeds " + str(rate/2))
	exit()

if args.data:
	s = args.data
else:
	s = input("Enter your data: ")

print("Input Stream: " + (''.join(map(bin,bytearray(s, 'utf-8')))) + "\n")
binout = ((''.join(map(bin,bytearray(s, 'utf-8')))).replace("b", "")).replace(" ", "")
print("Binout: %s \n" % (binout))

x = []
l = []

#------------------------------------------------------------------------------
# start sequence with 1800hz
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * start_sequence * t[:samples]))

# transform bitstream to corresponding frequency 
for i in binout:
	t = np.linspace(0, T, T*rate, endpoint=False)
	if i == '0':
		x.append(np.sin(2*np.pi * f1 * t[:samples]))
	if i == '1':
		x.append(np.sin(2*np.pi * f2 * t[:samples]))


# end sequence with 4000hz
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
t = np.linspace(0, T, T*rate, endpoint=False)
x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
#------------------------------------------------------------------------------

for i in x:
	for j in i:
		l.append(j);

l = np.array(l)

wavio.write(filename+".wav", l, rate, sampwidth=2)
