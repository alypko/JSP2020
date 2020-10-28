from itertools import chain
b = [[2,4,3],[1,5,6],[9],[7,9,0]]
i = list(chain.from_iterable(b))
print(i)