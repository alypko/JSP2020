import cmath as m 
l = 1j
a = m.sin(l)
print (a.real, a.imag)
b = m.cos(l)
print (b.real, b.imag)
print(a**2 + b **2 == 1)