#!/usr/bin/python3

class Ding(object):

    _dichte = { 'Fe' : ('Eisen' , 7.87),
                'Au' : ('Gold' , 19.32),
                'Ag' : ('Silber' , 10.5)}
    
    def __init__(self, symbol, volumen):
        self.__volumen = float(volumen)
        self._symbol = symbol

    def getMasse(self):
        return self.__volumen*self._dichte[self._symbol][1]
    
    def getVolumen(self):
        return self.__volumen

    def __str__(self):
        beschrb = 'Name: ' + str(self._dichte[self._symbol][0])\
        + ' Masse: ' + str(self.getMasse())
        return beschrb


