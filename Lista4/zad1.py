def mnozenie(lista):
    x = 1 
    for i in lista:
        x = x*i    
        return x

def dodawanie(lista):
    x = 0
    for i in lista:
        x = x+i
    return x 


A = range (3, 6)
print(list(A))
print(mnozenie(A))
print(dodawanie(A))

