import random

n=int(input("Enter range: "))

a=random.sample(range(1,1000),n)
for i in range(0,n):
        a[i]=random.randint(1,n//2+1)
print(a)
for i in range(0,n):
        if(a[i]==-99):
                continue
        for j in range(i+1,n):
                if(a[j]==-99):
                        continue
                if(a[i]==a[j]):
                        a[j]=-99
print(a)
for i in range(0,n-1):
        for j in range(i,n-1):
                if(a[j]==-99):
                        a[j],a[j+1]=a[j+1],a[j]
print(a)
