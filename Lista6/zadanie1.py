import trojkat as t
def main():
    a = int(input("Wprowadz bok trojkata a: "))
    b = int(input("Wprowadz bok trojkata b: "))
    c = int(input("Wprowadz bok trojkata c: "))

    if(a+b>c and a+c>b and b+c>a):
        print(t.perimeter(a, b, c))
        t.area(a, b, c)
        t.sprawdz(a, b, c)
        t.kat(a, b, c)
    else:
        print("nie mozna zbudowac trojkata")

main()