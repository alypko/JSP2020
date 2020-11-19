klucz={
    "a" : "y",
    "e" : "i",
    "i" : "o",
    "o" : "a",
    "y" : "e"
}

def szyfr(x):
    y=""
    k = list(klucz.keys())
    for charakter in x:
        if charakter in k:
            y+=klucz[charakter]
        else:
            y+=charakter
        
    return y

def deszyfr(x):
    y=""
    keys_values = klucz.items()
    odwortny_klucz = {value: key for key, value in keys_values}
    k=list(odwortny_klucz.keys())
    for charakter in x:
        if charakter in k:
            y+=odwortny_klucz[charakter]
        else:
            y+=charakter
    return y

a = input("tekst: ")
print(szyfr(a))  
print(deszyfr(szyfr(a)))