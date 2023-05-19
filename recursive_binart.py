import time
import random

def search(list,l,h,k):
        mid = (l+h)//2
        if(l>h):
                print("not found")
                return
        if(k<list[mid]):
                search(list,l,mid-1,k)
        elif(k>list[mid]):
                search(list,mid+1,h,k)
        elif(k==list[mid]):
                print("found at",mid)
                return

list = random.sample(range(1,1000),10)
list.sort()
print(list)
k = int(input("Enter key: "))
start = time.time()
search(list,0,len(list)-1,k)
end=time.time()
print(end-start)

