#!/usr/bin/python3
#Dieses Script stellt fünf einfache Multiplikationsaufgaben.
import random
import time

zeit1=time.time()
zeit2=0
zeit3=0
zahl1=1
zahl2=1
ergebins=1
eingabe=101
zahlaufg=int(input('Wie viele Aufgaben wollen sie lösen: '))
             
for a in range(zahlaufg):
             zahl1=random.randint(1,10)
             zahl2=random.randint(1,10)
             ergebnis = zahl1*zahl2
             print(zahl1,'*',zahl2)
             eingabe= int(input('Bitte geben sie die lösung ein: '))
             while eingabe != ergebnis:
                 print('Falsch')
                 eingabe= int(input('Bitte geben sie die lösung ein: '))
             print('richtig')
zeit2=time.time()
zeit3 = zeit2-zeit1
print('Sie haben %.2f Sekunden gebraucht um die Aufgaben zu lösen.'%zeit3)

             

            
