#必要なモジュールのインポート
import json
import numpy as np
import makeSound
from scipy.io import wavfile

#jsonファイルの読み込み
json_songData = open("./EMOTION.json","r")
songData = json.load(json_songData)
json_frequencies = open("./frequencies.json","r")
frequencies = json.load(json_frequencies)

#songの全体データを読み込み
fs = 44100
durationOfOneBeat = 60 / songData["tempo"]
duration = songData["length"] * durationOfOneBeat
filename = songData["songName"] + ".wav"
length_of_array = int(fs * (duration + 1))
array = np.zeros(length_of_array)

#各partのデータを処理
for part in songData["parts"]:
    if part["tone"] == "True":
        volume = part["volume"] / 100
        instrument = part["instrument"]
        for note in part["notes"]:
            tone = note[2]
            frequency = frequencies[tone[-1]][tone[:-1]]
            length_of_note = int(durationOfOneBeat * (note[1]-note[0]) * fs)
            offset = int(durationOfOneBeat * note[0] * fs)

            if instrument == "sine":
                array_note = makeSound.sine(length_of_note, frequency, volume, fs)

            if instrument == "sawtooth":
                array_note = makeSound.sawtooth(length_of_note, frequency, volume, fs)

            if instrument == "square":
                array_note = makeSound.square(length_of_note, frequency, volume, fs)
            
            if instrument == "triangular":
                array_note = makeSound.triangular(length_of_note, frequency, volume, fs)
            
            if instrument == "pulse":
                array_note = makeSound.pulse(length_of_note, frequency, volume, fs)

            #全体データに加算
            for n in range(length_of_note):
                array[offset+n] += array_note[n]
            
    elif part["tone"] == "False":
        instrument = part["instrument"]
        for note in part["notes"]:
            offset = int(durationOfOneBeat * note[0] * fs)
            if instrument == "Drums":
                array_note, length_of_note = makeSound.drums(note)
            
            #全体データに加算
            for n in range(length_of_note):
                array[offset+n] += array_note[n]

    s = part["partName"] + " processed."
    print(s)
        

for n in range(length_of_array):
    array[n] = (array[n] + 1) / 2 * 65536
    array[n] = int(array[n] + 0.5)
    if array[n] > 65535:
        array[n] = 65535
    elif array[n] < 0:
        array[n] = 0
    array[n] -= 32768
wavfile.write("EMOTION.wav",fs,array.astype(np.int16))