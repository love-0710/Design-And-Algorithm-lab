import time
import random
def search(list,k):
        for i in range(0,len(list)):
                if(list[i]==k):
                        return i
        return -1
list = random.sample(range(1,1000),10)
print(list)
start = time.time()
k = int(input("Enter the key: "))
m = search(list,k)
if(m==-1):
        print("Not found")
else:
        print("Found at",m)
end = time.time()
print(end-start)
