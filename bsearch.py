import time
import random

def search(list,k):
        low=0
        high=len(list)-1
        while(low<=high):
                mid=(low+high)//2
                if(k<list[mid]):
                        high=mid-1
                elif(k>list[mid]):
                        low=mid+1
                else:
                        return mid
        return -1

list = random.sample(range(1,1000),10)
list.sort()
print(list)
start = time.time()
k = int(input("Enter key "))
m = search(list,k)
if(m==-1):
        print("Not found")
else:
        print("found at",m)
end = time.time()
print(end-start)


