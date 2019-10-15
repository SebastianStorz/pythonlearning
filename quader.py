#!/usr/bin/python3
from ding import Ding

class Quader(Ding):

    def __init__(self, symbol, laenge, breite, hoehe):
        Ding.__init__(self, symbol, laenge*breite*hoehe)
        self.__laenge = laenge
        self.__breite = breite
        self.__hoehe = hoehe
        
    def __str__(self):
        beschrb = 'Material: ' + str(self._dichte[self._symbol][0]) + \
                  '\nLänge: '+ str(self.__laenge)+ \
                  '\nBreite: '+ str(self.__breite) +\
                  '\nHöhe: ' + str(self.__hoehe)
        return beschrb

    def __cmp__(self, other):
        a = self._getMasse()
        b = other._getMasse
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    



a = Quader('Au',10,10,10)
print(a)
b = Quader('Fe',10,10,10)
Quader('Au',10,10,10) < Quader('Fe',10,10,10)
