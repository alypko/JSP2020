import itertools

def perm(a):
    b = len(a)
    return list(itertools.permutations(a, b))


print(perm([1,2]))
