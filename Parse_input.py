import numpy as np


f = open("note_muzicale.txt")
input = f.read()

x = np.array(input.split("\n"))
musicalNotesList = []

for pair in x:
    elements = pair.split(" ")
    musicalNotesList.append([elements[0], float(elements[1])])

print(musicalNotesList)
