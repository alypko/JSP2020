import os 
from random import randint

def generator():
    rok = randint(1900, 2099)
    if rok<=1999:
        miesiac = randint(1,12)
    else:
        miesiac = randint(1,12) + 20
    np_miesiace = [1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32]
    p_miesiace = [4, 6, 9, 11, 24, 26, 29, 31]
    if miesiac in np_miesiace:
        dni=randint(1,31)
    elif miesiac in p_miesiace:
        dni = randint(1,30)
    else:
        if rok%4==0:
            if rok %100 == 0:
                if rok %400 == 0:
                    dni = randint (1, 29) #leap year 
                else:
                    dni = randint(1,28)
            else:
                dni = randint (1, 29)
        else: 
            dni = randint(1,28)
    foo = randint(1, 99999)
    return str('%02d'%(rok%100)+'%02d'%miesiac + '%02d'%dni + '%05d'%foo)


pesele = [generator() for i in range(10)]
try:
    open("PESEL.txt", "w").write("")
    for i in pesele:
        NewFile = open("PESEL.txt", "a")
        NewFile.write(i +"\n")
except:
    print("error")
print("success!")
