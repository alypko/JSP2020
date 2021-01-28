from itertools import combinations 

class Suma:
    def __init__(self, l):
        self.l = l

    def podlista(self):
        if len(self.l)<3:
            return 'Lista zawiera mniej niz 3 elementy'
        else:
            k=[list(x) for x in combinations(self.l, 3) if sum(x)==0]
            if(len(k)==0):
                return 'nie spelnia warunku'
            else:
                return k


t = [1, 2, 4, 5, 21, -3 ]

foo  = Suma(t)

print(foo.podlista())