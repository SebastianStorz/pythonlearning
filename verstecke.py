Python 3.7.4 (default, Jul  9 2019, 16:32:37) 
[GCC 9.1.1 20190503 (Red Hat 9.1.1-1)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def verstecke(satz,zeichen=1)
SyntaxError: invalid syntax
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	for i in satz:
		satz[i] += zeichen*random.randchar
	return satz
verstecke('Hallo'
	  
SyntaxError: invalid syntax
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	for i in satz:
		satz[i] += zeichen*random.randchar
	return satz

>>> verstecke('hallo')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    verstecke('hallo')
  File "<pyshell#8>", line 4, in verstecke
    satz[i] += zeichen*random.randchar
TypeError: string indices must be integers
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	for i in satz:
		rueckgabe=satz[i] + zeichen*random.randchar
	return rueckgabe

>>> verstecke('hallo')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    verstecke('hallo')
  File "<pyshell#11>", line 4, in verstecke
    rueckgabe=satz[i] + zeichen*random.randchar
TypeError: string indices must be integers
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	stelle=0
	for i in satz:
		rueckgabe=satz[stelle] + zeichen*random.randchar
		stelle+=1
	return rueckgabe

>>> verstecke('hallo')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    verstecke('hallo')
  File "<pyshell#14>", line 5, in verstecke
    rueckgabe=satz[stelle] + zeichen*random.randchar
AttributeError: module 'random' has no attribute 'randchar'
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	stelle=0
	for i in satz:
		rueckgabe=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	return rueckgabe

>>> import string
>>> verstecke('hallo')
'oE'
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	stelle=0
	for i in satz:
		rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	return rueckgabe

>>> verstecke('hallo')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    verstecke('hallo')
  File "<pyshell#21>", line 5, in verstecke
    rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
UnboundLocalError: local variable 'rueckgabe' referenced before assignment
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	stelle=0
	for i in satz:
		rueckgabe= rueckgabe +satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	return rueckgabe

>>> 
>>> verstecke('hallo')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    verstecke('hallo')
  File "<pyshell#24>", line 5, in verstecke
    rueckgabe= rueckgabe +satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
UnboundLocalError: local variable 'rueckgabe' referenced before assignment
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	stelle=0
	rueckgabe=''
	for i in satz:
		rueckgabe=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	return rueckgabe

>>> verstecke('hallo')
'oE'
>>> def verstecke(satz,zeichen=1):
	satz.upper()
	stelle=0
	rueckgabe=''
	for i in satz:
		rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	return rueckgabe

>>> verstecke('hallo')
'hGaSlIlSoX'
>>> s=hallo
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s=hallo
NameError: name 'hallo' is not defined
>>> s='hallo'
>>> s.upper()
'HALLO'
>>> def verstecke(satz,zeichen=1):
	stelle=0
	rueckgabe=''
	for i in satz:
		rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii)
		stelle+=1
	rueckgabe.upper()
	return rueckgabe

>>> verstecke('hallo')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    verstecke('hallo')
  File "<pyshell#37>", line 5, in verstecke
    rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii)
AttributeError: module 'string' has no attribute 'ascii'
>>> def verstecke(satz,zeichen=1):
	stelle=0
	rueckgabe=''
	for i in satz:
		rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	rueckgabe.upper()
	return rueckgabe

>>> verstecke('hallo')
'hIaRlLlSoU'
>>> verstecke('hallo asdf asdf')
'hUaJlYlQoM QaKsEdDfP KaBsWdSfA'
>>> def verstecke(satz,zeichen=1):
	stelle=0
	rueckgabe=''
	for i in satz:
		rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	rueckgabe.upper()
	print(type(rueckgabe))
	return rueckgabe

>>> verstecke('hallo asdf asdf')
<class 'str'>
'hNaOlFlHoF RaCsEdBfX QaGsKdSfU'
>>> def verstecke(satz,zeichen=1):
	stelle=0
	rueckgabe=''
	for i in satz:
		rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	return rueckgabe.upper()

>>> 
>>> verstecke('hallo asdf asdf')
'HGAYLVLUOS AAASYDOFR XATSGDGFC'
>>> #Die Funktion verstecke() wurde hier geschrieben -> verstecke(ein satz, anzahl von stellen die hinzugefügt werden)
>>> def verstecke(satz,zeichen=1):
	"""Diese Funktion fügt an einen Satz eine belibige anzahl Zeichen hinzu"""
	stelle=0
	rueckgabe=''
	for i in satz:
		rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	return rueckgabe.upper()

>>> def verstecke(satz,zeichen=1):
	"""Diese Funktion fügt an einen Satz eine belibige anzahl Zeichen hinzu"""
	import random
	import string
	stelle=0
	rueckgabe=''
	for i in satz:
		rueckgabe+=satz[stelle] + zeichen*random.choice(string.ascii_uppercase)
		stelle+=1
	return rueckgabe.upper()

>>> 
