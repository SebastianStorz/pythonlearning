#!usr/bin/python3
#Ein script für die Folge von Ulam
a=int(input('Bitte geben sie die Testzahl ein: '))
while a != 1:
    if a%2 == 0:
        a=a/2
        print(a)
    else:
        a = 3*a + 1
        print(a)
print('Das Script ist zuende')
