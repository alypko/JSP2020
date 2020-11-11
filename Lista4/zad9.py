def silnia(n):
    silnia = 1
    for i in range(1, int(n+1)):
        silnia *= i
    return silnia

a = int(input("Wprowadz liczbe calkowita: "))

print("Silnia liczby", a, "wynosi:",silnia(a))