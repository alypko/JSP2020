N = int(input("Wprowadz liczbe: "))
a = 0
b = 1
while True:
    print(a)
    Sum = a + b
    b = Sum
    a = Sum + a
    #print(b)
    print(Sum)
    if Sum > N:
        break
