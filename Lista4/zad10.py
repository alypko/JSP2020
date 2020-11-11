def nwd(a,b):
    while(b != 0):
        c = a % b 
        a = b
        b = c
    return a 


a = int(input("Wprowadz liczbe A: "))
b = int(input("Wprowadz liczbe B: "))

print("NWD liczb", a,"i", b, "wynosi", nwd(a,b))
