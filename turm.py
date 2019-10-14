#!/usr/bin/python3
#Die Türme von Hanoi

def bewege(n, von, nach, ueber):
    if n == 1:
        print('Lege eine Scheibe von',von,'nach',nach)
    else:
        print('.')
        bewege(n-1,von,ueber,nach)
        print('..')
        bewege(1,von,nach,ueber)
        print('...')
        bewege(n-1,ueber,nach,von)
        print('....')

print(bewege(2,1,2,3))
