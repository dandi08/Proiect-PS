import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import math
import matplotlib.pyplot as plt
import sounddevice
from scipy import signal

rate=44101
amp=10000
fullNote=2
note={}
noteCantec={}
note['LA4']=440
semiton=math.pow(2,1/12)
ton=math.pow(semiton,2)

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
    return np.sin(frecventa*timp)


def y(frecventa,timp):
    return signal.sawtooth(frecventa,timp)

def generate_song(noteCantec):
    signalComplet=[]
    for (nota, durata) in noteCantec:
        t=np.linspace(0,fullNote*1/durata,int(fullNote*1/durata*rate))
        signalCantec = [amp*x(note[nota],t)]
        np.concatenate(signalCantec)
    print(signalCantec)
    return signalCantec

def play_song(song):
    wav_wave = np.array(song, dtype=np.int16)
    print(wav_wave)
    sounddevice.play(wav_wave)
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


print(generate_song(noteCantec))
play_song(generate_song(noteCantec))





##print(note)



