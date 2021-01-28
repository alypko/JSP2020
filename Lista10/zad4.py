import xml.etree.ElementTree as ET
import ntpath
import os

class exchange:
    def __init__(self, p):
        self.p = p
        self.tree = ET.parse(self.p)
        self.root = self.tree.getroot()

    def available(self):  
            for currency in self.root.findall('pozycja'): 
                waluta = currency.find('nazwa_waluty').text
                kod = currency.find('kod_waluty').text
                print("Nazwa waluty:",waluta,"Kod:", kod)

    def Plnto(self):
        wybor = input("1 - z PLN na wybrana waluta / 2 - z wybranej waluty na PLN: ")
        kod = input("Podaj kod waluty: ")
        for currency in self.root.findall('pozycja'): 
                if(currency.find('kod_waluty').text == kod):
                    sr = currency.find('kurs_sredni').text.replace(',','.')
                    if (wybor == '1'):
                        zl = float(input("Podaj ilosc PLN: "))
                        y = float(currency.find('przelicznik').text)*zl / float(sr)
                        print(y, kod)
                    elif (wybor == '2'):
                        val = float(input("Podaj ilosc waluty: "))
                        y = float(sr) * val / float(currency.find('przelicznik').text)
                        print(y, "PLN")
                    else:
                        print("cos poszlo nie tak")

    def OnetoOther(self):
        kod1 = input("Podaj kod waluty1: ")
        kod2 = input("Podaj kod waluty2: ")
        wybor = input("1 - "+kod1+" na "+ kod2+"/ 2 - "+kod2+" na "+ kod1+": ")
        for currency1 in self.root.findall('pozycja'):
            sr1 = currency1.find('kurs_sredni').text.replace(',','.')
            if(currency1.find('kod_waluty').text == kod1):
                for currency2 in self.root.findall('pozycja'):
                    if(currency2.find('kod_waluty').text == kod2):
                        sr2 = currency2.find('kurs_sredni').text.replace(',','.')
                        if (wybor == '1'):
                            val = float(input("Podaj ilosc "+kod1+": "))
                            y = float(sr1)*val / float(sr2)
                            print(y, kod2)
                        elif (wybor == '2'):
                            val = float(input("Podaj ilosc "+kod2+": "))
                            y = float(sr2)*val / float(sr1)
                            print(y, kod1)
                        else:
                            print("cos jest nie tak")

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

path = input("Prosze podac sciezke do pliku .xml: ")
if(os.path.exists(path)):
   t = exchange((path))
   t.available()
else:
    print("taka sciezka nie istnieje")

