a = ["Kasia", "Basia", "Marek", "Darek"]
a.append("Joziek")
b = ["Ania", "Basia"]
a.extend(b)
a.sort()
print (a[3])
print (a[:2])
print (a[-2:])
while(a.count("Basia")):
    a.remove("Basia")
print(a)
print(len(a))
k=tuple(a)
print (k)