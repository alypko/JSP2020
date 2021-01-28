from math import pi


class Kolo:
    def __init__(self, r):
        self.r = r
    def area(self):
        return pi*self.r**2
    def perimeter(self):
        return 2*pi*self.r


k= Kolo(3)
print(k.area())
print(k.perimeter())
