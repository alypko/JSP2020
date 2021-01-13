def peselCheck():
    file= open("PESEL.txt", "r")
    f = file.readlines()
    new = open("OdkodowanePESELE.txt", "a")
    for p in f:
        CtrlNum=int(p[0])+3*int(p[1])+7*int(p[2])+9*int(p[3])+int(p[4])+3*int(p[5])+7*int(p[6])+9*int(p[7])+int(p[8])+3*int(p[9])+int(p[10])
        if(CtrlNum%10!=0):
            print("PESEL", p+"nie jest poprawny")
            file.close()
        else:
            
            d = int(p[4]+p[5])
            m = int(p[2]+p[3])
            r = int(p[0]+p[1])
            if(m>12):
                m-=20
                r+=2000
            else:
                r+=1900
            ur ='-'.join((str(d), str(m) ,str(r)))
            new.write("nr PESEL:"+p+"\n data urodzenia:"+ur+"\tplec: " + ("Kobieta" if int(p[9])%2 == 0 else "Mezczyzna"))
    file.close()
    new.close()

peselCheck()
            