a = input("Wprowadz napis: ")
if len(a)%2 == 0:
    print(a[:len(a)//2] + "Python" + a[len(a)//2:])
else:
    print (a[:len(a)//2] +"pytuxon" + a[len(a)//2:])
    