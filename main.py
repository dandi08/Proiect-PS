import sys
import numpy as np
import matplotlib
import scipy.io.wavfile

matplotlib.use('TkAgg')
import math
import matplotlib.pyplot as plt
import sounddevice
from scipy import signal

rate = 44100
amp = 10000
fullNote = 0.39 # we came to this value by the method called TRIAL AND ERROR
note = {}
noteCantec = {}
note['LA4'] = 440
note['P'] = 0
semiton = math.pow(2, 1 / 12)
ton = math.pow(semiton, 2)


def generate_notes(octava):
    if (octava > 1 and octava != 4):
        note['LA' + str(octava)] = note['LA' + str(octava - 1)] * 2
    elif (octava == 1):
        note['LA' + str(octava)] = note['LA4'] / math.pow(2, 4)
    note['DO' + str(octava)] = note['LA' + str(octava)] / semiton / math.pow(ton, 4)
    note['DO#' + str(octava)] = note['DO' + str(octava)] * semiton
    note['RE' + str(octava)] = note['DO' + str(octava)] * ton
    note['RE#' + str(octava)] = note['RE' + str(octava)] * semiton
    note['MI' + str(octava)] = note['RE' + str(octava)] * ton
    note['FA' + str(octava)] = note['MI' + str(octava)] * semiton
    note['FA#' + str(octava)] = note['FA' + str(octava)] * semiton
    note['SOL' + str(octava)] = note['FA' + str(octava)] * ton
    note['SOL#' + str(octava)] = note['SOL' + str(octava)] * semiton
    note['LA#' + str(octava)] = note['LA' + str(octava)] * semiton
    note['SI' + str(octava)] = note['LA' + str(octava)] * ton


for i in range(1, 11):
    generate_notes(i)


def sin(frecventa, timp):
    return np.sin(2 * frecventa * timp)


def generate_song(noteCantec):
    signalCantec = []
    for (nota, durata) in noteCantec:
        t = np.linspace(0, fullNote * 1 / durata, int(fullNote * 1 / durata * rate))
        signalCantec.append(amp * sin(note[nota], t))
    signalComplet = np.concatenate(signalCantec)
    return signalComplet


def play_song(song):
    wav_wave = np.array(song, dtype=np.int16)
    scipy.io.wavfile.write("proba123.wav", 44100, wav_wave)
    sounddevice.play(wav_wave, blocking=True)
    sounddevice.stop()


# simfonia a 9-a a lui Beethoven
noteCantec = [
    ('FA#6', 0.66),
    ('FA#6', 0.66),
    ('SOL6', 0.66),
    ('LA6', 0.66),
    ('LA6', 0.66),
    ('SOL6', 0.66),
    ('FA#6', 0.66),
    ('MI6', 0.66),
    ('RE6', 0.66),
    ('RE6', 0.66),
    ('MI6', 0.66),
    ('FA#6', 0.66),
    ('FA#6', 0.4),
    ('MI6', 2),
    ('MI6', 0.33),
]

f = open("note_muzicale.txt")
input = f.read()

x = np.array(input.split("\n"))
musicalNotesList = []

for pair in x:
    elements = pair.split(" ")
    musicalNotesList.append((elements[0], float(elements[1])))

play_song(generate_song(noteCantec))
