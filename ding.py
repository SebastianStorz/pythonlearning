#!/usr/bin/python3

class Ding(object):

    __dichte = { 'Fe' : ('Eisen' , 7.87),
                'Au' : ('Gold' , 19.32),
                'Ag' : ('Silber' , 10.5)}
    
    def __init__(self, symbol, volumen):
        self.__volumen = float(volumen)
        self._symbol = symbol

    def getMasse(self):
        return self.__volumen*self.__dichte[self._symbol][1]
    
    def getVolumen(self):
        return self.__volumen

    def __str__(self):
        beschrb = 'Symbol: ' + str(self.__dichte[self._symbol][1])\
        + ' Masse: ' + str(self.getMasse())
        return beschrb

krone= Ding('Au',100)
print(krone)
