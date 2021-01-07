import SzyfrCezara as ces
import os 
from time import strftime, localtime



def encode(path, k):
        f = open(path, "r")
        encrypt = ces.encrypt(f.read(), k)
        NewDir = input("Wprowadz sciezke katalogu: ")
        try:
            os.makedirs(NewDir)
            print(NewDir, 'created')
        except FileExistsError:
            print(NewDir, 'exsists')
        date = strftime("%Y%m%d", localtime())
        NewDir = NewDir + "/plik_zaszyfrowany" + str(k) + "_" + str(date) + ".txt"
        NewFile = open(NewDir, "w")
        NewFile.write(encrypt)
        NewFile.close()
        f.close()
    
#print(type(open(os.path.abspath("Lista1/zad2.py"), "r").read()))


path = input("Prosze podac sciezke: ")
if(os.path.exists(path)):
    przes = int(input("wprowadz przesuniecie: "))
    while(przes<1 or przes>10):
        przes = int(input("wprowadz przesuniecie: "))
    encode(path, przes)
else:
    print("taka sciezka nie istnieje")
