def jeden_dziesiec(x):
    if(x==0):
        b=""
    if(x==1):
        b ="jeden"
    elif(x==2):
        b="dwa"
    elif(x==3):
        b="trzy"
    elif(x==4):
        b="cztery"
    elif(x==5):
        b="piec"
    elif(x==6):
        b="szesc"
    elif(x==7):
        b="siedem"
    elif(x==8):
        b="osiem"
    elif(x==9):
        b="dziewiec"
    else:
        print("Error in jeden_dziesiec")
    return b
def jedenascie_dwadziescia(x):
    if(x==0):
        b=""
    if(x==1):
        b="jedenascie"
    elif(x==2):
        b="dwanascie"
    elif(x==3):
        b="trzynascie"
    elif(x==4):
        b="czternascie"
    elif(x==5):
        b="pietnascie"
    elif(x==6):
        b="szestnascie"
    elif(x==7):
        b="sedemnascie"
    elif(x==8):
        b="osiemnascie"
    elif(x==9):
        b="dziewietnascie"
    else:
        print("error in jedendscie_")
    return b
def dziesiatki(x):
    if(x==0):
        b=""
    if(x==1):
        b="dziesiec"
    elif(x==2):
        b="dwadziescia"
    elif(x==3):
        b="trzydziesci"
    elif(x==4):
        b="czerdziesci"
    elif(x==5):
        b="piecdziesiat"
    elif(x==6):
        b="szescdziesiat"
    elif(x==7):
        b="siedemdziesiat"
    elif(x==8):
        b = "osiemdziesiat"
    elif(x==9):
        b="dziewiecdziesiat"
    return b
def setki(x):
    if(x==0):
        b=""
    elif(x==1):
        b = "sto"
    elif(x==2):
        b="dwiescie"
    elif(x==3):
        b="trzysta"
    elif(x==4):
        b="czerysta"
    elif(x==5):
        b="piecset"
    elif(x==6):
        b="szeczset"
    elif(x==7):
        b="siedemset"
    elif(x==8):
        b="osiemset"
    elif(x==9):
        b="dziewiecset"
    else:
        print("error in setki")
    return b
def tysiace(x):
    if(x==0):
        b=""
    if(x==1):
        b="tysiac"
    elif(x==0):
        b=""
    else:
        print("error in tysiace")
    return b



def main(a):
    if(len(a)==0):
        print("Wprowadz dobra liczbe")
    elif(len(a)==1):
        print(jeden_dziesiec(int(a[0])))

    elif(len(a)==2):
        if(a[1]=="0"):
            print(dziesiatki(int(a[0])))
        elif(a[0]=="1"):
            print(jedenascie_dwadziescia(int(a[1])))

    elif(len(a)==3):
        if(a[1]=="0" and a[2]=="0"):
            print(setki(int(a[0])))
        elif(a[1]=="1"):
            print(setki(int(a[0])), jedenascie_dwadziescia(int(a[2])))
        else:
            print(setki(int(a[0])), dziesiatki(int(a[1])), jeden_dziesiec(int(a[2])))
    elif(len(a)==4):
        if(a[1]=="0" and a[2]=="0" and a[3]=="0"):
            print(tysiace(int(a[0])))
        elif(a[2]=="0" and a[3]=="0"):
            print(tysiace(int(a[0])), setki(int(a[1])))
        elif(a[1]=="0"):
            print(tysiace(int(a[0])), dziesiatki(int(a[2])), jeden_dziesiec(int(a[3])))
        elif(a[2]=="1"):
            print(tysiace(int(a[0])), setki(int(a[1])), jedenascie_dwadziescia(int(a[3])))
            
        else:
            print(tysiace(int(a[0])), setki(int(a[1])), dziesiatki(int(a[2])), jeden_dziesiec(int(a[3])))

    else:
        print("error in main")
    


a = list(input("Wprowadz liczbe od 1 do 1999: "))
print(a)
main(a)
