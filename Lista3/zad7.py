N = int(input("Wprowadz liczbe: "))
a = 0
b = 1
print(a)
print(b)
while True:
    Sum = a + b
    print(Sum)
    a = b
    b = Sum
    if Sum > N-2:
        break
