import SzyfrCezara as ces


a = input("Wpisz slowo/zdanie do szyfrowania: ")
k = int(input("Wpisz klucz do szyfrowania: "))

print("Twoj input wyglada nastepujaco: ", ces.encrypt(a, k))
print("Odrazu po deszyfrowaniu: ", ces.decrypt(ces.encrypt(a, k), k))