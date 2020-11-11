def suma(x):
    s = 0

    for i in list(range(1, int(x+1))):
        s+=1/i
    return s
a = int(input("Wprowadz liczbe wyrazow: "))
print(suma(a))