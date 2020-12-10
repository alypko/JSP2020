import random
import time 

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while(j>=0 and key<a[j]):
            a[j+1] = a[j]
            j-=1
        a[j+1]=key
    return a



l = [random.randint(0,20) for i in range(100)]
print(ins_sort(l), time.process_time())

