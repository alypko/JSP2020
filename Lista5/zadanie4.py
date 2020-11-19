klucz={
    "a" : "y",
    "e" : "i",
    "i" : "o",
    "o" : "a",
    "y" : "e"
}
print(list(klucz.keys()))
def szyfr(x):
    k = list(klucz.keys())
    for charakter in x:
        if charakter in k:
            x = x.replace(charakter, klucz[charakter])
    return x

def deszyfr(x):
    keys_values = klucz.items()
    odwortny_klucz = {value: key for key, value in keys_values}
    k=list(odwortny_klucz.keys())
    print(odwortny_klucz)
    for charakter in x:
        if charakter in k:
            x = x.replace(charakter, odwortny_klucz[charakter])
    print(x)

a = input("tekst: ")
print(szyfr(a))  
deszyfr(szyfr(a))