#Ein experiment für das Verhalten von Listen in funktionen -> Listen verändern sich in Funktionen und range ist ein Objekt

def quadriere(l):
    for i in range(len(l)):
        l[i]=l[i]*l[i]


liste=list(range(10))
print(liste)
quadriere(liste)
print(liste)
