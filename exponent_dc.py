def power(a,b):
        if a==1:
                return 1
        if k==0:
                return 0
        if b==1:
                return a
        if b%2==0:
                return power(a*a, b//2)
        else:
                return a*power(a*a, b//2)
n=int(input("Enter value of n: "))
k=int(input("Enter value of k: "))
print(power(n,k))






