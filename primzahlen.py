#!/usr/bin/python3
#Primzahlen aus einer Zahlenreihe

#Definition
def primzahl(zahl):
    if zahl<=2:
        prim=1
    else:
        for i in range(2,zahl):
            if zahl%i==0:
                prim=0
                break
        else:
                prim=1
    return prim
    
def eingabe():
    print('Ich ermittle alle Primzahlen in einem Intervall')
    a=int(input('Untere Intervallgrenze'))
    b=int(input('Obere Intervallgrenze'))
    return(a,b)

def verarbeitung(intervall):
    prim=[]
    (a,b)=intervall
    for i in range(a,b+1):
        if primzahl(i):
            prim+=[i]
    return prim

def ausgabe(primzahlen):
    print('Primzahlen')
    for zahl in primzahlen:
        print(zahl, end=' ')


#Hauptprogramm

intervall=eingabe()
primzahlListe=verarbeitung(intervall)
ausgabe(primzahlListe)
