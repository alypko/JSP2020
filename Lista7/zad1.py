import time 

def fib(n):
    x1 = time.time()
    n1 = 0
    n2 = 1
    for i in range(1, n-1):
        if(i==1):
            print(n1)
            pass
        if(i == 2):
            print(n2)
            pass
        nast = n1 + n2
        n1 = n2
        n2 = nast
        print(nast)
    x2 = time.time()
    print("Czas dzialania iteracyjnie:", x2-x1)

def fibRek(n):
    if(n==0):
        return 0
    elif(n>0 and n<=2):
        return 1
    else:
        return fibRek(n-2)+fibRek(n-1)


def main():
    a = int(input("ilosc: "))
    print("Wersja iteracyjnie:")
    fib(a)
    print("")
    x1 = time.time()
    for i in range(a):
        print(fibRek(i))
    print("Czas dzialania rekurencyjnie: ",time.time()-x1)
main()