import random
import time
def count_sort(arr,p):
        size=len(arr)
        count=[0]*10
        output=[0]*size
        for i in arr:
                index=i//p
                count[index%10]+=1
        for i in range(1,10):
                count[i]+=count[i-1]
        for i in range(size-1,-1,-1):
                index=arr[i]//p
                output[count[index%10]-1]=arr[i]
                count[index%10]-=1
        for i in range(0,size):
                arr[i]=output[i]
def radix(arr):
        t=time.time()
        m=max(arr)
        p=1
        while m//p>0:
                count_sort(arr,p)
                p*=10
        return time.time()-t
print("Sample\tBest Case\t\tAverage Case\t\tWorst Case")
for i in [10,100,1000,10000]:
        arr=(random.sample(range(10,5000000),i))
        p=arr
        q=arr
        p.sort()
        q.sort(reverse=True)
        print(f"{i}\t{radix(p)}\t{radix(arr)}\t{radix(q)}")



