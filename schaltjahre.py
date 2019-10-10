jahr=int(input('Bitte geben sie das Jahr ein: '))
if (jahr%400==0) or ((jahr%4==0)and(jahr%100==True)):
    print('Das Jahr',jahr,'ist ein Schaltjahr')
else:
    print('Das Jahr',jahr,'ist kein Schaltjahr')
 
