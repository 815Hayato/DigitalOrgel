import numpy as np
from scipy.io import wavfile

def sine(length_of_note, frequency, volume, fs):
    array_note = np.zeros(length_of_note)
    x = 0
    for n in range(length_of_note):
        array_note[n] += np.sin(2 * np.pi * x)
        delta = frequency / fs
        x += delta
        if x >= 1:
            x -= 1

    for n in range(int(fs * 0.01)):
        array_note[n] *= n / (fs * 0.01)
        array_note[length_of_note -n -1] *= n / (fs * 0.01)
    array_note *= volume
    return array_note

def sawtooth(length_of_note, frequency, volume, fs):
    array_note = np.zeros(length_of_note)
    x = 0
    for n in range(length_of_note):
        array_note[n] += -2 * x + 1
        delta = frequency / fs
        if 0 <= x and x < delta:
            t = x / delta
            d = -t*t + 2*t - 1
            array_note[n] += d
        if 1-delta < x and x <= 1:
            t = (x-1) / delta
            d = t*t + 2*t + 1
            array_note[n] += d
        x += delta
        if x >= 1:
            x -= 1
    
    for n in range(int(fs * 0.01)):
        array_note[n] *= n / (fs * 0.01)
        array_note[length_of_note -n -1] *= n / (fs * 0.01)
    array_note *= volume
    
    return array_note

def square(length_of_note, frequency, volume, fs):
    array_note = np.zeros(length_of_note)
    x = 0
    for n in range(length_of_note):
        if x < 0.5:
            array_note[n] += 1
        else:
            array_note[n] += -1
        delta = frequency / fs
        if 0 <= x and x < delta:
            t = x / delta
            d = -t*t + 2*t - 1
            array_note[n] += d
        elif 1-delta < x and x <= 1:
            t = (x-1) / delta
            d = t*t + 2*t + 1
            array_note[n] += d
        
        if 0.5 <= x and x < 0.5 + delta:
            t = (x-0.5) / delta
            d = -t*t + 2*t - 1
            array_note[n] -= d
        elif 0.5-delta < x and x <= 0.5:
            t = (x-0.5) / delta
            d = t*t + 2*t + 1
            array_note[n] -= d
        x += delta
        if x >= 1:
            x -= 1
    
    for n in range(int(fs * 0.01)):
        array_note[n] *= n / (fs * 0.01)
        array_note[length_of_note -n -1] *= n / (fs * 0.01)
    array_note *= volume
    
    return array_note

def triangular(length_of_note, frequency, volume, fs):
    array_note = np.zeros(length_of_note)
    x = 0

    for n in range(length_of_note):
        array_note[n] = np.abs(-4 * x + 2) - 1
        delta = frequency / fs
        x += delta
        if x >= 1:
            x -= 1
    
    for n in range(int(fs * 0.01)):
        array_note[n] *= n / (fs * 0.01)
        array_note[length_of_note -n -1] *= n / (fs * 0.01)
    array_note *= volume

    return array_note

def pulse(length_of_note, frequency, volume, fs):
    array_note = np.zeros(length_of_note)
    x = 0
    duty = 0.25
    for n in range(length_of_note):
        if x < duty:
            array_note[n] = 1
        else:
            array_note[n] = -1
            
        delta = frequency / fs
        if 0 <= x and x < delta:
            t = x / delta
            d = -t * t + 2 * t - 1
            array_note[n] += d
        elif 1 - delta < x and x <= 1:
            t = (x - 1) / delta
            d = t * t + 2 * t + 1
            array_note[n] += d
        
        if duty <= x and x < duty + delta:
            t = (x - duty) / delta
            d = -t * t + 2 * t - 1
            array_note[n] -= d
        elif duty - delta < x and x <= duty:
            t = (x - duty) / delta
            d = t * t + 2 * t + 1
            array_note[n] -= d

        x += delta
        if x >= 1:
            x -= 1

    for n in range(int(fs * 0.01)):
        array_note[n] *= n / (fs * 0.01)
        array_note[length_of_note -n -1] *= n / (fs * 0.01)
    array_note *= volume

    return array_note

def drums(note):
    instrument = note[1]
    volume = note[2] / 100
    if instrument == "bd":
        fs, array_note = wavfile.read("Drums/BD.wav")
        array_note = array_note.astype(np.float)
        length_of_note = len(array_note)
        np.random.seed(0)
        for n in range(length_of_note):
            array_note[n] += 32768 + (np.random.rand() - 0.5)
            array_note[n] = array_note[n] / 65536 *2 -1
            array_note[n] *= volume

    elif instrument == "sn":
        fs, array_note = wavfile.read("Drums/SN.wav")
        array_note = array_note.astype(np.float)
        length_of_note = len(array_note)
        np.random.seed(0)
        for n in range(length_of_note):
            array_note[n] += 32768 + (np.random.rand() - 0.5)
            array_note[n] = array_note[n] / 65536 *2 -1
            array_note[n] *= volume

    elif instrument == "hh":
        fs, array_note = wavfile.read("Drums/HH.wav")
        array_note = array_note.astype(np.float)
        length_of_note = len(array_note)
        np.random.seed(0)
        for n in range(length_of_note):
            array_note[n] += 32768 + (np.random.rand() - 0.5)
            array_note[n] = array_note[n] / 65536 *2 -1
            array_note[n] *= volume     

    return array_note, length_of_note