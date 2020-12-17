import random
import time 

def bubbleSort(a):
    x1=time.time()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if(a[j]>a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    x2=time.time()
    print(a, x2-x1)
l = [random.randint(0,20) for i in range(500)]
bubbleSort(l)