import math as m

def perimeter(a, b, c):
    return (a+b+c)


def area(a, b, c):
    p = perimeter(a, b, c)/2
    print( m.sqrt(p*(p-a)*(p-b)*(p-c)))

def sprawdz(a, b, c):
    
        if(a==b or b==c or a==c):
            print("Trojkat jest rownoramienny")
        elif(a==b==c):
            print("Trojkat jest rownoboczny")
        else:
            print("trojkat roznoboczny")
    
def kat(a, b, c):
    boki = [a, b, c]
    boki = sorted(boki, reverse=True)
    if(boki[0]**2>boki[1]**2+boki[2]**2):
        print("trojkat jest rozwartokatny")
    elif(boki[0]**2==boki[1]**2+boki[2]**2):
        print("trojkat jest prostokatny")
    else:
        print("trojkat jest ostrokatny")

