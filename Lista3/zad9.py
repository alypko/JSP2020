m = int(input("Podaj liczbe wierszy: "))
n = int(input("Podaj liczbe l=kolumn: "))

A = [[None] * m for i in range(0, n)]
# print(A)
A[m-1][n-1] = m * n
print(A)