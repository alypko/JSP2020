def powtarzannie(x):
    return list(dict.fromkeys(x))


print(powtarzannie([1, 1, 2, 3, 3,]))