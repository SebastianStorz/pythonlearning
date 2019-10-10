#!usr/bin/python3
#Ein Script zur simulation der Vermehrung von Bakterien

hour = 0
bac = 100

while hour < 48:
    print('Stunde:',hour,'    ',bac,'Bakterien')
    bac= bac*4
    hour+=1
print('Nach zwei Tagen sind es',bac,'Backterien.')
