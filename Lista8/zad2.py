import re
import os
from time import strftime, localtime
import SzyfrCezara as ces


def decode(path):
    regex = re.compile(r'\d+')
    NewDir = input("Wprowadz sciezke do zapisania odszyfrowanego pliku: ")
    for filename in os.listdir(path):
        k = [int(x) for x in regex.findall(filename)][0]
        filename = path+"/"+filename
        f = open(filename, "r")
        decrypt = ces.decrypt(f.read(), k)
        try:
            os.makedirs(NewDir)
            print(NewDir, 'created')
        except FileExistsError:
            print(NewDir, 'exsists')
        date = strftime("%Y%m%d", localtime())
        NewDir = NewDir + "/plik_odszyfrowany" + str(k) + "_" + str(date) + ".txt"
        NewFile = open(NewDir, "w")
        NewFile.write(decrypt)
        NewFile.close()
        f.close()







path = input("Prosze podac sciezke(do katalogu) do zaszyfrowanych plikow: ")
if(os.path.exists(path)):
    decode(path)
else:
    print("taka sciezka nie istnieje")



#regex = re.compile(r'\d+')
#print([int(x) for x in regex.findall("plik_zaszyfrowany4_20210106")][0])