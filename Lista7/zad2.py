import random
import time 

def ins_sort(a):
    x1 = time.time()
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while(j>=0 and key<a[j]):
            a[j+1] = a[j]
            j-=1
        a[j+1]=key
    x2= time.time()
    print(a,x2-x1)



l = [random.randint(0,20) for i in range(100)]
ins_sort(l)

