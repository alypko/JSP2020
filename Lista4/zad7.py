def trojkat_pascala(liczba_wierszy):
    p=[1]
    for i in range(liczba_wierszy):
        print(p)
        p = [1] + [a+b for a,b in zip(p[1:], p[:-1])] + [1]

a = int(input("Wprowadz liczbe wierszy trojkata pascala: "))
trojkat_pascala(a)