
import sys
import numpy

def operacje(info):
    dane = [int(i) for i in info if type(i) == int or i.isdigit()]
    wyniki = [numpy.mean(dane), numpy.std(dane), numpy.var(dane)]
    return wyniki

if len(sys.argv) == 1:
    x = sys.stdin.read()
else:
    x = sys.argv[1:]
print("Średnia: ", operacje(x)[0], "Odchylenie standardowe: ", operacje(x)[1], "Wariancja: ", operacje(x)[2])