import time
import random
def partition(a,l,h):
        i=l-1
        pivot=a[h]
        for j in range(l,h):
                if a[j]<=pivot:
                        i+=1
                        a[i],a[j]=a[j],a[i]
        a[i+1],a[h]=a[h],a[i+1]
        return i+1
def sort(a,l,h):
        if l<h:
                p=partition(a,l,h)
                sort(a,l,p-1)
                sort(a,p+1,h)

print("Sample\tBest Case\t\tAverage Case\t\tWorst Case")
for i in [10,100,500]:
        arr=(random.sample(range(10,5000000),i))
        p=arr
        q=arr
        p.sort()
        q.sort(reverse=True)
        t1=time.time()
        sort(p,0,len(p)-1)
        t2=time.time()
        sort(arr,0,len(arr)-1)
        t3=time.time()
        sort(q,0,len(q)-1)
        t4=time.time()
        print(f"{i}\t{t2-t1}\t{t3-t2}\t{t4-t3}")

