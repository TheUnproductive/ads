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

def short(T, rate, x, f1, f2, samples):
	binpref = ((''.join(map(bin,bytearray("s", 'utf-8')))).replace("b", "")).replace(" ", "")
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))

def standard(T, rate, x, f1, f2, samples):
	binpref = ((''.join(map(bin,bytearray("standard", 'utf-8')))).replace("b", "")).replace(" ", "")
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))

def custom(T, rate, x, f1, f2, file, samples):
	binpref = ((''.join(map(bin,bytearray("custom", 'utf-8')))).replace("b", "")).replace(" ", "")
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))
	binpref = ((''.join(map(bin,bytearray(str(f1), 'utf-8')))).replace("b", "")).replace(" ", "")
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))
	binpref = ((''.join(map(bin,bytearray(str(f2), 'utf-8')))).replace("b", "")).replace(" ", "")
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))
	binpref = ((''.join(map(bin,bytearray(str(rate), 'utf-8')))).replace("b", "")).replace(" ", "")
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))
	binpref = ((''.join(map(bin,bytearray(str(file), 'utf-8')))).replace("b", "")).replace(" ", "")
	for i in binpref:
		t = np.linspace(0, T, T*rate, endpoint=False)
		if i == '0':
			x.append(np.sin(2*np.pi * f1 * t[:samples]))
		if i == '1':
			x.append(np.sin(2*np.pi * f2 * t[:samples]))
