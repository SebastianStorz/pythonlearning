#!/usr/bin/python
print('Dieses Programm berechnet die Prüfstelleder ISBN Nummer')
isbn= input('Die ISBN Nummer ohne Prüfziffer: ')
a = 0
summe= 0
while a < 9:
    summe +=(int(isbn[a]))*(a+1)
    a += 1
prüfziffer = summe %11
print(prüfziffer)
