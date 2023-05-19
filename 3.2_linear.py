import random
import time
p=random.sample(range(1,1000000),20000)
elem=0
start=time.time()
k=0
for i in range(0,len(p)):
        if elem==p[i]:
                print("Found at ", i)
                k=1
                break
if k==0:
        print("Not Found")
print("Time Taken:",time.time()-start)

