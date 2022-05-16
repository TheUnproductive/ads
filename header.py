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
	print(binpref)
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))

def writeheaderdata_int(T, rate, x, f1, f2, samples, integer):
	binpref = bin(integer).replace("0b", "")
	print(binpref)
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))

def writeheaderdata_padded(T, rate, x, f1, f2, samples, binary):
	binpref = format(binary, '#009b').replace("0b", "")
	print(binpref)
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))

def short(T, rate, x, f1, f2, ms, file_len):
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), 0)
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), file_len)

def standard(T, rate, x, f1, f2, samples, ms, file_len):
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), ms)
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), file_len)

def custom(T, rate, x, f1, f2, file_len, ms=5, file_type="txt"):
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), 1)
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), int(f1//1000))
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), int(f2//1000))
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), int(rate//1000))
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), ms)
	print("file_type " + file_type)
	writeheaderdata(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), str(file_type))
	writeheaderdata_int(T, 48000, x, 22000.0, 23000.0, 48000//(1000//ms), file_len)