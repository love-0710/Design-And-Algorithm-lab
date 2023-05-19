import random
import time

def binary_search(list1,n):
        f=0
        l=len(list1)-1
        while f<=l:
                mid=(f+l)//2
                if list1[mid]==n:
                        print("Found at ",mid);
                        return
                elif n>list1[mid]:
                        f=mid+1
                else:
                        l=mid-1
        print("Not Found")
def binary_rec(l1,n,f,l):
        if f>l:
                print("Not found")
                return
        else:
                mid=(f+l)//2
                if(l1[mid]==n):
                        print("Found at ",mid)
                        return
                elif n>l1[mid]:
                        binary_rec(l1,n,mid+1,l)
                else:
                        binary_rec(l1,n,f,mid-1)


p=random.sample(range(1,1000000),10)
p.sort()
start=time.time()
elem=p[(len(p)-1)//2]                #BEST CASE
#elem=random.choice(p)                #AVERAGE CASE
#elem=0                               #WORST CASE
binary_search(p,elem)
#binary_rec(p,elem,0,len(p)-1)
print("Time Taken: ",time.time()-start)
