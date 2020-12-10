import random
import time 

def bubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if(a[j]>a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a
l = [random.randint(0,20) for i in range(500)]
print(bubbleSort(l), time.process_time())