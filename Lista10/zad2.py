from itertools import combinations 


class sublist:
    def __init__(self, l):
        self.l = l

    def sublists(self):
        new = list()
        for i in range(len(self.l)+1):
            new.extend([list(k) for k in combinations(self.l, i)])
        return new



t = [1,2,3]
foo = sublist(t)
print(foo.sublists())