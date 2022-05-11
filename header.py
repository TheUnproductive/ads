import numpy as np

def start(T, rate, x, start_sequence, samples):
	t = np.linspace(0, T, T*rate, endpoint=False)
	x.append(np.sin(2*np.pi * start_sequence * t[:samples]))

def stop(T, rate, x, stop_sequence, samples):
	t = np.linspace(0, T, T*rate, endpoint=False)
	x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
	t = np.linspace(0, T, T*rate, endpoint=False)
	x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))
	t = np.linspace(0, T, T*rate, endpoint=False)
	x.append(np.sin(2*np.pi * stop_sequence * t[:samples]))

def writeheaderdata(T, rate, x, f1, f2, samples, string):
	binpref = ((''.join(map(bin,bytearray(string, 'utf-8')))).replace("b", "")).replace(" ", "")
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))

def short(T, rate, x, f1, f2, samples):
	writeheaderdata(T, rate, x, f1, f2, samples, "s")

def standard(T, rate, x, f1, f2, samples):
	writeheaderdata(T, rate, x, f1, f2, samples, "standard")

def custom(T, rate, x, f1, f2, file, samples, ms, breaker_freq):
	writeheaderdata(T, 44100, x, 2.0, 22048.0, 44100//(1000//ms), "custom")
	start(T, 44100, x, breaker_freq, 44100//(1000//ms))
	writeheaderdata(T, 44100, x, 2.0, 22048.0, 44100//(1000//ms), str(f1))
	start(T, 44100, x, breaker_freq, 44100//(1000//ms))
	writeheaderdata(T, 44100, x, 2.0, 22048.0, 44100//(1000//ms), str(f2))
	start(T, 44100, x, breaker_freq, 44100//(1000//ms))
	writeheaderdata(T, 44100, x, 2.0, 22048.0, 44100//(1000//ms), str(rate))
	start(T, 44100, x, breaker_freq, 44100//(1000//ms))
	writeheaderdata(T, 44100, x, 2.0, 22048.0, 44100//(1000//ms), str(ms))
	start(T, 44100, x, breaker_freq, 44100//(1000//ms))
	writeheaderdata(T, 44100, x, 2.0, 22048.0, 44100//(1000//ms), str(file))