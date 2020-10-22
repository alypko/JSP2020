import math as m 

a = input("Podaj pierwszy bok trojkata:") 
b = input("Podaj drugi bok trojkata:")
kat = input("POdaj kąt między tymi bokami:")
pole_trojkata = 0.5 * float(a) * float(b) * m.sin(float(kat) * m.pi/180)

print ("Pole trójkatą wynosi: ", pole_trojkata)