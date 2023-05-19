a=int(input("Enter the prime no.:  "))
f=0
for i in range(2,a/2+1):
        if (a%i==0):
                f=1
                break
if f==0 and a!=1:
        print("prime")
else:
        print("not prime")

