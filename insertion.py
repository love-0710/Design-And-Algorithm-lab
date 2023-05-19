import random
import time

def insertion_sort(a):
        for i in range(1,len(a)):
                j=i
                while(j>0 and a[j-1]>a[j]):
                        a[j],a[j-1] = a[j-1],a[j]
                        j=j-1

n=int(input("Enter range:"))
a=random.sample(range(1,2000),n)

print("Average case:")
print(a)
start=time.time()
insertion_sort(a)
end=time.time()
print("Sorted list")
print(a)
print(end-start)

print("\n\nWorst case:")
a.sort(reverse=True)
print(a)
start=time.time()
insertion_sort(a)
end=time.time()
print("Sorted list:")
print(a)
print(end-start)


