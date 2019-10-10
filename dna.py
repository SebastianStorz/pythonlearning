#!/usr/bin/python3
#Ein script zur ermittlung aller möglichen DNA paare
dna = ['AT','TA','GC','CG']
for a in dna:
    for b in dna:
        for c in dna:
            for d in dna:
                print(a,b,c,d)
