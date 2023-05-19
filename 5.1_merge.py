import random
import time
def sort(a):
        if len(a)<=1:
                return a
        p=sort(a[:len(a)//2])
        q=sort(a[len(a)//2:])
        return combine(p,q)

def combine(p,q):
        r=[]
        j=0
        k=0
        while j<len(p) and k<len(q):
                if p[j]<q[k]:
                        r.append(p[j])
                        j+=1
                else:
                        r.append(q[k])
                        k+=1
        if j==len(p):
                r=r+q[k:]
        elif k==len(q):
                r=r+p[j:]
        return r

print("Sample\tBest Case\t\tAverage Case\t\tWorst Case")
for i in [10,100,500]:
        arr=(random.sample(range(10,5000000),i))
        p=arr
        q=arr
        p.sort()
        q.sort(reverse=True)
        t1=time.time()
        sort(p)
        t2=time.time()
        sort(arr)
        t3=time.time()
        sort(q)
        t4=time.time()
        print(f"{i}\t{t2-t1}\t{t3-t2}\t{t4-t3}")

