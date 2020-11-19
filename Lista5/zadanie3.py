  
def RzymToInt(x):
    rzym = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    p = 0
    odp = 0
    n = len(x)
    for i in range(n-1, -1, -1):
        print(i)
        if rzym[x[i]] >= p:
            odp += rzym[x[i]]
        else:
            odp -= rzym[x[i]]
 
        
        p = rzym[x[i]]
 
    print(odp)
 
a=input("Wprowadz licze rzymska: ")
RzymToInt(a)