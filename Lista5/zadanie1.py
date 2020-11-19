def str_to_liczba(a):
    b = 0
    x = 0
    if(len(a) == 1):
        if(a[0]=="jeden"):
            x=1
        elif(a[0]=="dwa"):
            x=2
        elif(a[0]=="trzy"):
            x=3
        elif(a[0]=="cztery"):
            x=4
        elif(a[0]=="piec"):
            x=5
        elif(a[0]=="szeszc"):
            x=6
        elif(a[0]=="siedem"):
            x=7
        elif(a[0]=="osiem"):
            x=8
        elif(a[0]=="dziewiec"):
            x=9
        elif(a[0]=="dziesiec"):
            x=10
        elif(a[0]=="jedennascie"):
            x=11
        elif(a[0]=="dwanascie"):
            x=12
        elif(a[0]=="trzynascie"):
            x=13
        elif(a[0]=="czternascie"):
            x=14
        elif(a[0]=="pietnascie"):
            x=15
        elif(a[0]=="szesnascie"):
            x=16
        elif(a[0]=="siedemnascie"):
            x=17
        elif(a[0]=="osiemnascie"):
            x=18
        elif(a[0]=="dziewietnascie"):
            x=19
        elif(a[0]=="dwadziescia"):
            x=20
        elif(a[0]=="trzydziesci"):
            x=30
        elif(a[0]=="czetdziesci"):
            x=40
        elif(a[0]=="piecdziesiat"):
            x=50
        else:
            x = None
    

    elif(len(a)==2):

        if(a[0]=="dwadziescia"):
            b = 2
        elif(a[0]=="trzydziesci"):
            b=3
        elif(a[0]=="czetdziesci"):
            b=4
        elif(a[0]=="piecdziesiat"):
            b=5
        if (a[1] == 'jeden'):
            x = 1
        elif (a[1] == 'dwa'):
            x= 2
        elif (a[1] == 'trzy'):
            x = 3
        elif (a[1] == 'cztery'):
            x = 4
        elif (a[1] == 'piec'):
            x = 5
        elif (a[1] == 'szesc'):
            x = 6
        elif (a[1] == 'siedem'):
            x = 7
        elif (a[1] == 'osiem'):
            x = 8
        elif (a[1] == 'dziewiec'):
            x = 9
        else:
            x = None
            b = None    
    
    if(x==None or b == None):
        print("Podaj dobra liczbe")
    elif(len(a)==1):
        print(x)
    else:
        print(str(b)+str(x))

a = input("Wprowadz slownie liczbe od 1 do 59: ")
c = a.split(" ")
print(c)
print(len(c))
str_to_liczba(c)