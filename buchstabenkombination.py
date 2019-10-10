#!/usr/bin/python3
#alle kombinationen aus den Grossbuchstaben
alphabet= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            print(a+b-c)
