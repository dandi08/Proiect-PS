import sys
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import math
import matplotlib.pyplot as plt
import sounddevice
from scipy import signal

rate=44100
amp=10000
fullNote=4
note={}
noteCantec={}
note['LA4']=440
note['P']=0
semiton=math.pow(2,1/12)
ton=math.pow(semiton,2)
##np.set_printoptions(threshold=1000000)

def generate_note(octava):
    if(octava>1 and octava!=4):
        note['LA'+str(octava)]=note['LA'+str(octava-1)]*2
    elif(octava==1):
        note['LA'+str(octava)]=note['LA4']/math.pow(2,4)
    note['DO'+str(octava)]=note['LA'+str(octava)]/semiton/math.pow(ton,4)
    note['DO#'+str(octava)]=note['DO'+str(octava)]*semiton
    note['RE'+str(octava)]=note['DO'+str(octava)]*ton
    note['RE#'+str(octava)]=note['RE'+str(octava)]*semiton
    note['MI'+str(octava)]=note['RE'+str(octava)]*ton
    note['FA'+str(octava)]=note['MI'+str(octava)]*semiton
    note['FA#'+str(octava)]=note['FA'+str(octava)]*semiton
    note['SOL'+str(octava)]=note['FA'+str(octava)]*ton
    note['SOL#'+str(octava)]=note['SOL'+str(octava)]*semiton
    note['LA#'+str(octava)]=note['LA'+str(octava)]*semiton
    note['SI'+str(octava)]=note['LA'+str(octava)]*ton

for i in range(4,11):
    generate_note(i)
for i in range(1,4):
    generate_note(i)

##print(note)

def x(frecventa,timp):

   # x=np.sin(np.pi*frecventa*timp)
    print(frecventa,timp)
    return 1

def sawtooth(frequency, time):
    "Undă în formă de dinți de fierăstrău"
    x = frequency * time
    return x - np.floor(x) - 1/2
def y(frecventa,timp):
    return signal.sawtooth(frecventa,timp)

def generate_tone(frequency, duration):
    "Generează un ton pur de frecvență dată, pentru durata cerută"
    print(frequency)
    n_samples = duration * rate
    time = np.linspace(0, duration, int(n_samples + 1))
    test=x(1,1)
    return 1

def generate_song(noteCantec):
    signalCantec=[]
    for (nota, durata) in noteCantec:
        t=np.linspace(0,fullNote*1/durata,int(fullNote*1/durata*rate))
        signalCantec.append(amp*sawtooth(note[nota],t))
    signalComplet=np.concatenate(signalCantec)
    ##print(signalCantec)
    return signalComplet

def play_song(song):
    wav_wave = np.array(song, dtype=np.int16)
    sounddevice.play(wav_wave,blocking=True)
    sounddevice.stop()

noteCantec = [
    ('FA#4', 2), ('MI4', 2),
    ('RE4', 2), ('DO#4', 2),
    ('SI3', 2), ('LA3', 2),
    ('SI3', 2), ('DO#4', 2),
    ('FA#4', 2), ('MI4', 2),
    ('RE4', 2), ('DO#4', 2),
    ('SI3', 2), ('LA3', 2),
]


f = open("note_muzicale.txt")
input = f.read()

x = np.array(input.split("\n"))
musicalNotesList = []

for pair in x:
    elements = pair.split(" ")
    musicalNotesList.append((elements[0], float(elements[1])))
# print(noteCantec)
# print(musicalNotesList)
# print(np.shape(noteCantec))
# print(np.shape(musicalNotesList))
# print(type(noteCantec[0][1]))
# print(type(musicalNotesList[0][1]))

plt.xlabel("Timp")
plt.ylabel("Intensitate")
plt.plot(generate_tone(440, 0.01))
plt.show()




