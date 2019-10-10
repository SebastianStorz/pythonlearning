#!/usr/bin/python3
#zahlenraten.py
import random
zahl=random.randint(1,100)
raten=101
while zahl != raten:
    raten=int(input('Bitte geben sie eine Zahl ein: '))
    if raten < zahl:
        print('Höher!')
    elif raten > zahl:
        print('Geringer!')
print('Richtig, die Zahl war:',zahl)
