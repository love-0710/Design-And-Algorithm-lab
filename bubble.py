import random
import time

def bubble_sort(a):
        for i in range(0,len(a)):
                for j in range(0,len(a)-i-1):
                        if(a[j]>a[j+1]):
                                a[j],a[j+1]=a[j+1],a[j]

n=int(input("Enter range: "))
a = random.sample(range(1,2000),n)

print("Average case:\n")
print(a)
start = time.time()
bubble_sort(a)
end=time.time()
print("\n\nSorted list:\n")
print(a)
print(end-start)

print("\n\nWorst case:\n")
a.sort(reverse=True)
print(a)
start=time.time()
bubble_sort(a)
end=time.time()
print("\n\nSorted list:\n")
print(a)
print(end-start)

