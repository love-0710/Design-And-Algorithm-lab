import random
import time

def bubblesort(p):
        start=time.time()
        for i in range(len(p)-1):
                for j in range(len(p)-1-i):
                        if p[j]>p[j+1]:
                                p[j],p[j+1]=p[j+1],p[j]
        return time.time()-start

def insertionSort(p):
        start=time.time()
        for j in range(1,len(p)):
                i=j
                while i>0 and p[i-1]>p[i]:
                        p[i],p[i-1]=p[i-1],p[i]
                        i-=1
        return time.time()-start

print("Sample Size\t\tWorst Case\t\tAvg Case\t\tBest Case")
for i in [10,100,1000]:
        p=random.sample(range(1,1000000),i)
        a=p
        a.sort()                    #best case
        b=p
        b.sort(reverse=True)       #worst case
        print(f"{i}\t\t{insertionSort(a)}\t{insertionSort(p)}\t{insertionSort(b)}")


