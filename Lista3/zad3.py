a = int(input("Podaj wspolczynnik a: "))
b = int(input("Podaj wspolczynnik b: "))
c = int(input("Podaj wspolczynnik c: "))
delta = b**2 - 4*a*c
pierw = delta**0.5
if a == 0:
    print("To nie jest rownanie kwadratowe!!")
elif delta>0:
    x1 = (-b - pierw)/2*a
    x2 = (-b + pierw)/2*a
    print("x1==", x1, "x2 ==", x2)
    pass
elif delta == 0:
    x0 = -b/(2*a)
    print("x0==", x0)
    pass
else:
    print("To rownanie nie ma rozwiazan")
    pass