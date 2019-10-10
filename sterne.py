#!/usr/bin/python3
#Dieses Script schreibt schöne Punkte

muster=int(input('Bitte geben sie das gewollte muster ein. (1,2,3)'))
sterne=0

if muster == 1:
    for i in range(4):
        print('* * * *')
if muster == 2:
    for i in range(5):
        print((i+1)*'* ')
if muster == 3:
    for i in range(5):
        print((4-i)*' ',(i+1)*'* ')
